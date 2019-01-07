#!/usr/bin/env bash

PACKAGE_NAME=$1

python monkey.py ${PACKAGE_NAME}

CURRENT_TIME=`date +%Y%m%d%H%M`

echo $CURRENT_TIME > buildtime
sh +x dumplog.sh logcat.txt monkeylog.txt ${PACKAGE_NAME}

sh +x report.sh meminfo.txt $CURRENT_TIME
