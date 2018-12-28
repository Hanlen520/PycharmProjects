#!/bin/sh

printAPKInfo()
{
	echo "----------------------------------------------------------------------------------" >> mail_content
	echo "-----------------------APK Information--------------------------------------------" >> mail_content
	cat output >> mail_content
}

dumpcrashlog()
{
	local logfile=$1
#	echo "----------------------------------------------------------------------------------" 
#	echo "Crash information from logcat"
#	echo "----------------------------------------------------------------------------------"
	grep "ek.smartinputv5 >>> com.cootek.smartinputv5 <<<" ${logfile} > logcat_crash.txt
	grep "crash" ${logfile} | grep "com.cootek.smartinputv5" >> logcat_crash.txt
	count=`grep -c '' logcat_crash.txt`
	echo "-----------------COUNT----------------" >> logcat_crash.txt
	echo $count >> logcat_crash.txt
	echo "" >> logcat_crash.txt
#	echo "----------------------------------------------------------------------------------"
#	echo "Crash information from monkey log"
#	echo "----------------------------------------------------------------------------------"
	local monkeylog=$2
	grep "CRASH in com.cootek.smartinputv5" ${monkeylog} > monkeylog_crash.txt
	count=`grep -c '' monkeylog_crash.txt`
	echo "-----------------COUNT----------------" >> monkeylog_crash.txt
	echo $count >> monkeylog_crash.txt
}

dumpANRlog()
{
	local logfile=$1
#	echo "---------------------------------------------------------------------------------"
#	echo "ANR information from logcat"
#	echo "---------------------------------------------------------------------------------"
	grep "ANR in com.cootek.smartinputv5" ${logfile} > logcat_ANR.txt
	count=`grep -c '' logcat_ANR.txt`
	echo "-----------------COUNT----------------" >> logcat_ANR.txt
	echo $count >> logcat_ANR.txt
}

printmail()
{
	echo "----------------------------------------------------------------------------------" > mail_content
	echo "Crash information from logcat" >> mail_content
	echo "----------------------------------------------------------------------------------" >> mail_content
	cat logcat_crash.txt >> mail_content
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
