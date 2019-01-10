#!/bin/bash


# 可用output_temp代替以下信息
#mkdir apk_tmp/
#cp TouchPal.apk apk_tmp/
## 反编译TouchPal.apk
#cd apk_tmp/ && apktool d TouchPal.apk
#version=`grep optpage_version_summary TouchPal/res/values/strings.xml |cut -f2 -d ">" |cut -f 1 -d "<"`
## 返回到上一次的工作目录
#cd -
#rm -r apk_tmp/


event=990000
timestamp=`date +%Y-%m-%d`
android_version="Android `adb shell getprop ro.build.version.release`"
device="emulator"
#size=`adb shell dumpsys window displays | grep "init" | tr -d $'\r' | awk '{print $1}' | cut -d"=" -f 2`
#density=`adb shell dumpsys window displays | grep "init" | tr -d $'\r' | awk '{print $2}'`
#display=${size}/${density}
#/var/lib/jenkins/workspace/MonkeyTest/
peak_mem=`awk -F , '{print $2}' /var/lib/jenkins/workspace/MonkeyTest/logs/csv/t_u.csv|sort -n|tail -n 1`
least_mem=`awk -F , '{print $2}' /var/lib/jenkins/workspace/MonkeyTest/logs/csv/t_u.csv|sort -n|sed -n '2p'`
end_mem=`awk -F , '{print $2}' /var/lib/jenkins/workspace/MonkeyTest/logs/csv/t_u.csv|tail -n 1`
crash_num_line=`grep -n "COUNT" /var/lib/jenkins/workspace/MonkeyTest/logcat_crash.txt|cut -f1 -d :`
crash_num_line=`expr ${crash_num_line} + 1`
crash_num=`eval "sed -n '${crash_num_line}p' /var/lib/jenkins/workspace/MonkeyTest/logcat_crash.txt"`
mkdir filter_logcat/
dir=`ls|grep 2019`
cp ${dir}/log.zip filter_logcat/
cd filter_logcat/ && unzip log.zip && cd -
python /opt/data/cootekime/MonkeyScripts/log_filter.py filter_logcat/logcat.txt com.cootek.smartinputv5 ANR.txt FC.txt anr_list
python /opt/data/cootekime/MonkeyScripts/filter_anr.py filter_logcat/crashlog.txt
anr_crash=`head -n 1 result`
anr_num=`grep COUNT ANR.txt|awk '{print $4}'`
fc_num=`grep COUNT FC.txt|awk '{print $4}'`
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
cat FC.txt >> mail_report
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
