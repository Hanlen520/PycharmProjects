#!/bin/bash


PACKAGE_NAME=$1

# find apk download links
# copy build result, renamed it output_temp
cp /var/lib/jenkins/workspace/IME_BRANCH_BUILD/BUILD_OUTPUT/build_result.txt output_temp
# apk info
#cat output_temp | head -n 37 | tail -n +3 > output
cat output_temp > apkinfo
# download apk, named TouchPal.apk
APK_DOWNLOAD_URL=`awk '/Apk download url:/{getline; print}' output_temp`
# download url
echo ${APK_DOWNLOAD_URL}
wget -O TouchPal.apk ${APK_DOWNLOAD_URL}
# delete temp file
rm -rf output_temp

#mkdir dump_files
# run monkey
#python monkey.py ${PACKAGE_NAME}

START_TIME=`date +%Y%m%d%H%M`
echo "开始时间：${START_TIME}" > buildtime

python /var/lib/jenkins/opt/data/cootekime/MonkeyScripts/monkey.py ${PACKAGE_NAME}

CURRENT_TIME=`date +%Y%m%d%H%M`
echo "结束时间：${CURRENT_TIME}" >> buildtime

sh +x /var/lib/jenkins/opt/data/cootekime/MonkeyScripts/dumplog.sh logcat.txt monkeylog.txt

OBJ_DOWNLOAD_URL=`grep files.zip output`
# download file, named obj.zip
wget -O obj.zip ${OBJ_DOWNLOAD_URL}
unzip obj.zip

# https://developer.android.com/ndk/guides/ndk-stack?hl=zh-cn
#/opt/data/cootekime/android-ndk-r9c/ndk-stack -sym obj/local/armeabi/ < logcat.txt  > crashlog.txt
#/opt/data/cootekime/android-ndk-r9c/ndk-stack -sym backup_files/obj/obj/local/armeabi-v7a/ < logcat.txt  > crashlog.txt

#Run monkey test memery report shell: report.sh
#sh +x /data/jenkins_home/jenkins/opt/data/cootekime/report.sh meminfo.txt ${CURRENT_TIME}
mkdir output_monkey
/bin/bash +x /var/lib/jenkins/opt/data/cootekime/MonkeyScripts/report.sh meminfo.txt
#Zip log files
#adb -s A49947C561B2 pull /sdcard/netCapture.pcap ./
#zip -m log.zip netCapture.pcap
zip -m log.zip logcat.txt
zip -m log.zip monkeylog.txt
zip -m log.zip meminfo.txt
#zip -m log.zip crashlog.txt
#zip -m log.zip shop_meminfo.txt
#mkdir ${CURRENT_TIME}
cp log.zip output_monkey/
cp mail_content output_monkey/
rm -f mail_content
cat output_monkey/report >> output_monkey/mail_content

#ftpcmd uploadfromdir ${CURRENT_TIME} cootek-file/ime_daily/monkeytest/${CURRENT_TIME}
# 暂时注释掉以下一行
#osscmd uploadfromdir  ${CURRENT_TIME}/ oss://cootek-file/ime_daily/monkeytest/${CURRENT_TIME} --check_point=check_point_file
#Upload log.zip to aliyunoss
#python /opt/data/cootekime/cootek_tools/put.py log.zip cootek-file/ime_daily/monkeytest/${CURRENT_TIME}/log.zip

#Print monkey test logfiles download url.
# 暂时注释掉以下两行
#echo "Downloads:" > address
#echo http://oss.aliyuncs.com/cootek-file/ime_daily/monkeytest/${CURRENT_TIME}/log.zip >> address
