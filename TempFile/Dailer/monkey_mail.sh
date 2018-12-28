#!/bin/bash
serialNum=$1
mkdir apk_tmp/
cp Dialer.apk apk_tmp/
cd apk_tmp/ && apktool d Dialer.apk
version=`grep optpage_version_summary TouchPal/res/values/strings.xml |cut -f2 -d ">" |cut -f 1 -d "<"`
cd -
rm -r apk_tmp/
event=990000
timestamp=`date +%Y-%m-%d`
android_version="Android `adb -s ${serialNum} shell getprop ro.build.version.release`"
device=`adb -s ${serialNum} shell getprop ro.product.model`
display=`adb -s ${serialNum} shell dumpsys window |grep Display |head -n 1 |cut -f 2 -d =| awk '{print $1}'`
peak_mem=`awk -F , '{print $2}' logs/csv/t_u.csv|sort -n|tail -n 1`
least_mem=`awk -F , '{print $2}' logs/csv/t_u.csv|sort -n|sed -n '2p'`
end_mem=`awk -F , '{print $2}' logs/csv/t_u.csv|tail -n 1`
crash_num_line=`grep -n "COUNT" logcat_crash.txt|cut -f1 -d :`
crash_num_line=`expr $crash_num_line + 1`
crash_num=`eval "sed -n '${crash_num_line}p' logcat_crash.txt"`
mkdir filter_logcat/
dir=`ls|grep 2017`
cp $dir/log.zip filter_logcat/
cd filter_logcat/ && unzip log.zip && cd -
python log_filter.py filter_logcat/logcat.txt com.phonedialer.contact ANR.txt FC.txt anr_list
anr_num=`grep -E "^COUNT" ANR.txt |awk '{print $4}'`
fc_num=`grep -E "^COUNT" FC.txt |awk '{print $4}'`
echo "-------------------------NEW--------------------" > mail_report
echo "Device :${device}/${android_version}/${display}" >> mail_report
echo "Date :${timestamp}" >> mail_report
echo "Version :${version}">> mail_report
echo "Event :${event}" >> mail_report
echo "Crash : ${crash_num} crash; ${fc_num} FC; ${anr_num} ANR" >> mail_report
echo "\n" >> mail_report
echo "1.monkeytest版本为daily;" >> mail_report
echo "\n" >> mail_report
echo "2.${anr_num}次ANR引起的native crash, 共${anr_num}个问题" >> mail_report
cat anr_list >> mail_report
echo "\n" >> mail_report
cat ANR.txt >> mail_report
echo "\n" >> mail_report
echo "3.有${fc_num}次FC,共${fc_num}个问题" >> mail_report
cat FC.txt >> mail_report
echo "\n" >> mail_report
echo "4.Memory least value ${least_mem},peak value ${peak_mem}, memory test completed value ${end_mem}" >> mail_report
echo "\n" >> mail_report
rm -r filter_logcat/
rm FC.txt
rm ANR.txt
