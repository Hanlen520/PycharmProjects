#!/bin/bash

DEVICE_NOT_FOUND=60
DOWNLOAD_FAIL=61
INSTALL_FAIL=62

#Detect device
serialNumber=$1
if [ `adb devices |grep $serialNumber |wc -l` != 1 ];then
    echo "Device is not exist!"
	exit $DEVICE_NOT_FOUND
fi

#Download apk
url_path=$2
#APK_DOWNLOAD_URL=`grep aligned.apk ${url_path} | awk '{print $4}'`
cp /var/lib/jenkins/jobs/IME_Project_Dialer_Build/workspace/ime_project_dialer/app/build/outputs/apk/app-online-debug.apk Dialer.apk

#Install apk
adb -s $serialNumber install -r Dialer.apk
if [ $? != 0 ];then
    exit $INSTALL_FAIL
fi

#Carry out monkey
python monkey.py $serialNumber

#Handle log
CURRENT_TIME=`date +%Y%m%d%H%M`
echo $CURRENT_TIME > buildtime
dumplog.sh logcat.txt monkeylog.txt
/opt/data/cootekime/android-ndk-r9c/ndk-stack -sym obj/local/armeabi/ < logcat.txt  > crashlog.txt
#Run monkey test memery report shell: report.sh
report.sh meminfo.txt $CURRENT_TIME
count=1
while [ `adb devices |grep $serialNumber |wc -l` != 1 ]
do
    count=$((count+1))
    echo "Wait for device $serialNumber"
	sleep 20
    if [ $count = 15 ];then
	    exit $DEVICE_NOT_FOUND
	fi
done
#Zip log files
zip -m log.zip logcat.txt
zip -m log.zip monkeylog.txt
zip -m log.zip meminfo.txt
zip -m log.zip crashlog.txt
zip -m log.zip heapInfo.txt

mkdir ${CURRENT_TIME}
cp log.zip ${CURRENT_TIME}/
osscmd uploadfromdir  ${CURRENT_TIME}/ oss://cootek-file/ime_daily/monkeytest/${CURRENT_TIME} --check_point=check_point_file

#Print monkey test logfiles download url.
echo "Downloads:" > address
echo http://oss.aliyuncs.com/cootek-file/ime_daily/monkeytest/${CURRENT_TIME}/log.zip >> address
cat $2 >> mail_content
exit 0
