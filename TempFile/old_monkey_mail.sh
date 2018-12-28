#!/bin/bash
filter_anr()
{
	cat /dev/null > ANR.txt
	anr_num=`grep "ANR in com.cootek.smartinputv5" $1|awk -F ANR '{print $2}'|sort|uniq|wc -l`
	if [ `grep "ANR in com.cootek.smartinputv5" $1|wc -l` != 0 ];then
		grep "ANR in com.cootek.smartinputv5" $1|awk -F ANR '{print $2}'|sort|uniq > anr_list
		while read line
		do
			linenum=`grep -n "${line}" $1|head -n 1|awk '{print $1}'|cut -f1 -d :|awk '{print int($0)}'`
			while [ ${linenum} != 0 ]
			do
				if [ `eval "sed -n '${linenum}p' $1|grep DEBUG|wc -l"` = 0 ];then
					eval "sed -n '${linenum}p' $1 >> ANR.txt"
					linenum=$(($linenum+1))
				else
					linenum=0
				fi
			done
		done < anr_list
	fi
	echo "-------------------------------------" >> ANR.txt
	echo "OutOfMemoryError" >> ANR.txt
	grep "Caused by: java.lang.OutOfMemoryError"  $1 >> ANR.txt
}

filter_fc()
{
	cat /dev/null > FC.txt
	fc_num=`grep "Force-killing crashed app com.cootek.smartinputv5" $1|grep "crash"|wc -l`
	if [ `grep "Force-killing crashed app com.cootek.smartinputv5" $1 |grep "crash"|wc -l` != 0 ];then
		grep "Force-killing crashed app com.cootek.smartinputv5" $1 > fc_list
		while read line
		do
			linenum=`grep -n "${line}" $1|awk '{print $1}'|cut -f1 -d :`
			linenum=`expr $linenum + 0`
			while [ ${linenum} != 0 ]
			do
				if [ `eval "sed -n '${linenum}p' $1|grep FATAL|wc -l"` = 0 ];then
					eval "sed -n '${linenum}p' $1 >> FC.txt"
					linenum=$(($linenum-1))
				else
					eval "sed -n '${linenum}p' $1 >> FC.txt"
					linenum=0
				fi
			done
		done < fc_list
	fi
}

mkdir apk_tmp/
cp TouchPal.apk apk_tmp/
cd apk_tmp/ && apktool d TouchPal.apk
version=`grep optpage_version_summary TouchPal/res/values/strings.xml |cut -f2 -d ">" |cut -f 1 -d "<"`
cd -
rm -r apk_tmp/
event=990000
timestamp=`date +%Y-%m-%d`
android_version="Android `adb -s A49947C561B2 shell getprop ro.build.version.release`"
device=`adb -s A49947C561B2 shell getprop ro.product.model`
display=`adb -s A49947C561B2 shell dumpsys window |grep Display |head -n 1 |cut -f 2 -d =| awk '{print $1}'`
peak_mem=`awk -F , '{print $2}' /var/lib/jenkins/jobs/MonkeyTest/workspace/logs/csv/t_u.csv|sort -n|tail -n 1`
least_mem=`awk -F , '{print $2}' /var/lib/jenkins/jobs/MonkeyTest/workspace/logs/csv/t_u.csv|sort -n|sed -n '2p'`
end_mem=`awk -F , '{print $2}' /var/lib/jenkins/jobs/MonkeyTest/workspace/logs/csv/t_u.csv|tail -n 1`
crash_num_line=`grep -n "COUNT" /var/lib/jenkins/jobs/MonkeyTest/workspace/logcat_crash.txt|cut -f1 -d :`
crash_num_line=`expr $crash_num_line + 1`
crash_num=`eval "sed -n '${crash_num_line}p' /var/lib/jenkins/jobs/MonkeyTest/workspace/logcat_crash.txt"`
mkdir filter_logcat/
dir=`ls|grep 2017`
cp $dir/log.zip filter_logcat/
cd filter_logcat/ && unzip log.zip && cd -
filter_fc filter_logcat/logcat.txt
filter_anr filter_logcat/logcat.txt
python /opt/data/cootekime/MonkeyScripts/filter_anr.py filter_logcat/crashlog.txt
anr_crash=`head -n 1 result`
#filter_crash filter_logcat/crashlog.txt
echo "-------------------------NEW--------------------" > mail_report
echo "Device :${device}/${android_version}/${display}" >> mail_report
echo "Date :${timestamp}" >> mail_report
echo "Version :${version}">> mail_report
echo "Event :${event}" >> mail_report
echo "Crash : ${anr_num} crash; ${fc_num} FC; ${anr_crash} ANR" >> mail_report
echo "\n" >> mail_report
echo "1.monkeytest版本为daily;" >> mail_report
echo "\n" >> mail_report
echo "2.${anr_crash}次ANR引起的native crash, 共${anr_num}个问题" >> mail_report
cat anr_list >> mail_report
echo "\n" >> mail_report
cat ANR.txt >> mail_report
echo "\n" >> mail_report
echo "3.有${fc_num}次FC,共${fc_num}个问题" >> mail_report
tac FC.txt >> mail_report
echo "\n" >> mail_report
echo "4.Memory least value ${least_mem},peak value ${peak_mem}, memory test completed value ${end_mem}" >> mail_report
echo "\n" >> mail_report
dump_num=`sed -n '2p' result`
echo "5.TouchPal Crash dump: ${dump_num}个" >> mail_report
cat result >> mail_report
echo "\n" >> mail_report
rm -r filter_logcat/
rm FC.txt
rm ANR.txt
