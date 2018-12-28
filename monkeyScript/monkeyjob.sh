#!/usr/bin/env bash

PACKAGE_NAME=$1

python monkey.py

CURRENT_TIME=`date +%Y%m%d%H%M`

echo $CURRENT_TIME > buildtime
dumplog.sh logcat.txt monkeylog.txt



