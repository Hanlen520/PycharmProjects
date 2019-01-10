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
echo ${APK_DOWNLOAD_URL}
wget -O TouchPal.apk ${APK_DOWNLOAD_URL}
# delete temp file
rm -rf output_temp

START_TIME=`date +%Y%m%d%H%M`
echo "Starting Time: ${START_TIME}" > buildtime

# run monkey
python /var/lib/jenkins/opt/data/cootekime/MonkeyScripts/monkey.py ${PACKAGE_NAME}

END_TIME=`date +%Y%m%d%H%M`
echo "End Time：${END_TIME}" >> buildtime

sh +x /var/lib/jenkins/opt/data/cootekime/MonkeyScripts/dumplog.sh logcat.txt monkeylog.txt

mkdir output_monkey

#Run monkey test memery report shell: report.sh
/bin/bash +x /var/lib/jenkins/opt/data/cootekime/MonkeyScripts/report.sh meminfo.txt

zip -m log.zip logcat.txt
zip -m log.zip monkeylog.txt
zip -m log.zip meminfo.txt

cp log.zip output_monkey/
cp mail_content output_monkey/
rm -f mail_content
cat output_monkey/report >> output_monkey/mail_content
cat buildtime >> output_monkey/mail_content
