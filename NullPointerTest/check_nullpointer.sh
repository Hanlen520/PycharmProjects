#!/usr/bin/env bash
# Author: Shengjie.Liu
# Date: 2019-03-27
# Version: 1.1
# Description:  遍历Activity,检查空指针问题
# How to use: sh +x check_nullpointer.sh

# 如果有反编译后的文件夹存在，先清空当前环境
if [[ -d "apkFile" ]]; then
    rm -r AC_list_filter Activity_List apkFile log.txt all_log.txt
fi

WORKSPACE=`pwd`
# apk地址
echo "Please enter the apk file address:"
read apk_address
# apk包名
#pkg_name=$(aapt dump badging ${apk_address} | grep package: | sed 's/ //g' | tr -d $'\r' | cut -d"'" -f2)
# 反编译
apktool d ${apk_address} -o apkFile
# 获取安卓manifest文件
ANDROID_MANIFEST=${WORKSPACE}/apkFile/AndroidManifest.xml
# 包名
pkg_name=$(sed -n '1p' ${ANDROID_MANIFEST} | awk '{for(i=1;i<=NF;i++){print $i;}}' | grep "package" | awk -F '"' '{print $2}')
# 通过FindActivity.py获取Activity列表
python FindActivity.py ${ANDROID_MANIFEST}
# 删除包含"loader.a.ActivityN1/loader.a.ActivityP0/loader.a.ActivityP1/loader.a.ActivityP2"的Activity
sed '/loader.a.ActivityN1/d;/loader.a.ActivityP0/d;/loader.a.ActivityP1/d;/loader.a.ActivityP2/d' Activity_List > AC_list_filter
# 运行python nullpointer.py，输出log在指定文件夹
echo "Starting..."
python NullPointer.py ${pkg_name}

# 全部log
adb logcat -d -v threadtime > ${WORKSPACE}/all_log.txt
# error log
adb logcat -d -v long "AndroidRuntime:E" "*:S" > ${WORKSPACE}/log.txt

echo "log文件：${WORKSPACE}/log.txt"
