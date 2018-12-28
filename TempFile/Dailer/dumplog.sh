#!/bin/sh

printAPKInfo()
{
	echo "----------------------------------------------------------------------------------" >> mail_content
	echo "-----------------------APK Information--------------------------------------------" >> mail_content
}

dumpcrashlog()
{
	local logfile=$1
	grep "crash" ${logfile} > logcat_crash.txt
	grep "com.phonedialer.contact" logcat_crash.txt > logcat_crash_contact.txt
	grep "AndroidRuntime" ${logfile} > logcat_runtime.txt
	grep "FATAL" ${logfile} > logcat_fatal.txt
	grep "ANR" ${logfile} > logcat_anr.txt
	count=`grep -c '' logcat_runtime.txt`
	echo "-----------------COUNT----------------" >> logcat_crash.txt
	echo $count >> logcat_runtime.txt
	echo "" >> logcat_runtime.txt
	local monkeylog=$2
	grep "CRASH in com.phonedialer.contact" ${monkeylog} > monkeylog_crash.txt
	count=`grep -c '' monkeylog_crash.txt`
	echo "-----------------COUNT----------------" >> monkeylog_crash.txt
	echo $count >> monkeylog_crash.txt
}

dumpANRlog()
{
	local logfile=$1
	grep "ANR in com.phonedialer.contact" ${logfile} > logcat_ANR.txt
	count=`grep -c '' logcat_ANR.txt`
	echo "-----------------COUNT----------------" >> logcat_ANR.txt
	echo $count >> logcat_ANR.txt
}

printmail()
{
	echo "----------------------------------------------------------------------------------" > mail_content
	echo "Crash information from logcat" >> mail_content
	echo "----------------------------------------------------------------------------------" >> mail_content
	echo "Logcat crash contact" >> mail_content
	cat logcat_crash_contact.txt >> mail_content
	echo "Logcat runtime" >> mail_content
	cat logcat_runtime.txt >> mail_content
	echo "" >> mail_content
	echo "Logcat fatal" >> mail_content
	cat logcat_fatal.txt >> mail_content
	echo "" >> mail_content
	echo "Logcat anr" >> mail_content
	cat logcat_anr.txt >> mail_content
	echo "" >> mail_content
	
	echo "----------------------------------------------------------------------------------" >> mail_content
	echo "Crash information from monkey log" >> mail_content
	echo "----------------------------------------------------------------------------------" >> mail_content
	cat monkeylog_crash.txt >> mail_content
	echo "" >> mail_content
	
	echo "---------------------------------------------------------------------------------" >> mail_content
	echo "ANR information from logcat" >> mail_content
	echo "---------------------------------------------------------------------------------" >> mail_content
	cat logcat_ANR.txt >> mail_content

	printAPKInfo
}

LOGCAT_FILE=$1
MONKEY_LOG=$2

dumpcrashlog $LOGCAT_FILE $MONKEY_LOG
dumpANRlog $LOGCAT_FILE

printmail
