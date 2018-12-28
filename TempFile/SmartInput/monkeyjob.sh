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
cp $url_path output_temp
line_num=`awk '/com.cootek.smartinputv5\/international\/online\/release\/TouchPal_smartinputv5_international/{print NR}' output_temp`
let start_num=line_num-36
let end_num=line_num+4
awk 'NR>40&&NR<79' output_temp > output
rm -r output_temp
APK_DOWNLOAD_URL=`grep -E "http://.*.release.aligned.apk" $url_path |grep com.cootek.smartinputv5/international`
wget -O TouchPal.apk ${APK_DOWNLOAD_URL}
if [ $? != 0 ];then
    exit $DOWNLOAD_FAIL
fi

#Install apk
adb -s $serialNumber install -r TouchPal.apk
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
adb devices
#Zip log files
zip -m log.zip logcat.txt
zip -m log.zip monkeylog.txt
zip -m log.zip meminfo.txt
zip -m log.zip crashlog.txt
zip -m log.zip shop_meminfo.txt

mkdir ${CURRENT_TIME}
cp log.zip ${CURRENT_TIME}/
osscmd uploadfromdir  ${CURRENT_TIME}/ oss://cootek-file/ime_daily/monkeytest/${CURRENT_TIME} --check_point=check_point_file

#Print monkey test logfiles download url.
echo "Downloads:" > address
echo http://oss.aliyuncs.com/cootek-file/ime_daily/monkeytest/${CURRENT_TIME}/log.zip >> address
exit 0
