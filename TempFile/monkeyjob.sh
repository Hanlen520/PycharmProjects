#!/bin/bash


PACKAGE_NAME=$1

# find apk download links
# change the path of build result
cp /var/lib/jenkins/jobs/IME_Daily_Build_v2/workspace/BUILD_OUTPUT/build_result.txt output_temp
line_num=`awk '/com.cootek.smartinputv5\/international\/online\/release\/TouchPal_smartinputv5_international/{print NR}' output_temp`
let start_num=line_num-36
let end_num=line_num+4
cat output_temp | head -n ${end_num} | tail -n +${start_num} > output

APK_DOWNLOAD_URL=`grep 'com.cootek.smartinputv5/international/online/release/TouchPal_smartinputv5_international' output_temp`
# download apk, named TouchPal.apk
wget -O TouchPal.apk ${APK_DOWNLOAD_URL}
rm -r output_temp

mkdir dump_files
# run monkey
python /opt/data/cootekime/MonkeyScripts/monkey.py

CURRENT_TIME=`date +%Y%m%d%H%M`

echo $CURRENT_TIME > buildtime
/opt/data/cootekime/MonkeyScripts/dumplog.sh logcat.txt monkeylog.txt

#OBJ_DOWNLOAD_URL=`grep obj.zip output`
OBJ_DOWNLOAD_URL=`grep files.zip output`

# 下载文件并将名字指定为obj.zip
wget -O obj.zip ${OBJ_DOWNLOAD_URL}

unzip obj.zip

# https://developer.android.com/ndk/guides/ndk-stack?hl=zh-cn
#/opt/data/cootekime/android-ndk-r9c/ndk-stack -sym obj/local/armeabi/ < logcat.txt  > crashlog.txt
/opt/data/cootekime/android-ndk-r9c/ndk-stack -sym backup_files/obj/obj/local/armeabi-v7a/ < logcat.txt  > crashlog.txt

#Run monkey test memery report shell: report.sh
/opt/data/cootekime/MonkeyScripts/report.sh meminfo.txt $CURRENT_TIME
#echo -e "CooTek01"|sudo -S /opt/data/cootekime/sdk/platform-tools/adb kill-server
#echo -e "CooTek01"|sudo -S /opt/data/cootekime/sdk/platform-tools/adb start-server
#DEVICE_NOT_FOUND=65
#while [ `adb devices |grep A49947C561B2 |wc -l` != 1 ]
#do
#    count=$((count+1))
#    echo "Wait for device"
#	sleep 20
#    if [ $count = 15 ];then
#	    exit $DEVICE_NOT_FOUND
#	fi
#done
#Zip log files
#adb -s A49947C561B2 pull /sdcard/netCapture.pcap ./
#zip -m log.zip netCapture.pcap
zip -m log.zip logcat.txt
zip -m log.zip monkeylog.txt
zip -m log.zip meminfo.txt
zip -m log.zip crashlog.txt
#zip -m log.zip shop_meminfo.txt
mkdir ${CURRENT_TIME}
cp log.zip ${CURRENT_TIME}/
#ftpcmd uploadfromdir ${CURRENT_TIME} cootek-file/ime_daily/monkeytest/${CURRENT_TIME}
osscmd uploadfromdir  ${CURRENT_TIME}/ oss://cootek-file/ime_daily/monkeytest/${CURRENT_TIME} --check_point=check_point_file
#Upload log.zip to aliyunoss
#python /opt/data/cootekime/cootek_tools/put.py log.zip cootek-file/ime_daily/monkeytest/${CURRENT_TIME}/log.zip

#Print monkey test logfiles download url.
echo "Downloads:" > address
echo http://oss.aliyuncs.com/cootek-file/ime_daily/monkeytest/${CURRENT_TIME}/log.zip >> address
