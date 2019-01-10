#!/usr/bin/env bash

printAPKInfo()
{
	echo "----------------------------------------------------------------------------------" >> mail_content
	echo "-----------------------APK Information--------------------------------------------" >> mail_content
	cat output >> mail_content
}

dumpcrashlog()
{
	local logfile=$1
	local pkname=$3
#	echo "----------------------------------------------------------------------------------"
#	echo "Crash information from logcat"
#	echo "----------------------------------------------------------------------------------"
#	grep "ek.smartinputv5 >>> com.cootek.smartinputv5 <<<" ${logfile} > logcat_crash.txt
	grep "crash" ${logfile} | grep ${pkname} >> logcat_crash.txt
	count=`grep -c '' logcat_crash.txt`
	echo "-----------------COUNT----------------" >> logcat_crash.txt
	echo $count >> logcat_crash.txt
	echo "" >> logcat_crash.txt
#	echo "----------------------------------------------------------------------------------"
#	echo "Crash information from monkey log"
#	echo "----------------------------------------------------------------------------------"
	local monkeylog=$2
	grep "CRASH in ${pkname}" ${monkeylog} > monkeylog_crash.txt
	count=`grep -c '' monkeylog_crash.txt`
	echo "-----------------COUNT----------------" >> monkeylog_crash.txt
	echo $count >> monkeylog_crash.txt
}

dumpANRlog()
{
	local logfile=$1
	local pkgname=$2
#	echo "---------------------------------------------------------------------------------"
#	echo "ANR information from logcat"
#	echo "---------------------------------------------------------------------------------"
	grep "ANR in ${pkgname}" ${logfile} > logcat_ANR.txt
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

#	printAPKInfo
}

LOGCAT_FILE=$1
MONKEY_LOG=$2
PACKAGE_NAME=$3

dumpcrashlog $LOGCAT_FILE $MONKEY_LOG ${PACKAGE_NAME}
dumpANRlog $LOGCAT_FILE ${PACKAGE_NAME}

printmail
