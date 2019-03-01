#!/usr/bin/env bash
# Author: Shengjie.Liu
# Date: 2019-01-24
# Version: 1.0
# Description:  获取活动名


window=$(adb shell dumpsys activity activities | sed -En -e '/Running activities/,/Run #0/p' | awk 'NR==3{print}' | awk '{print $5}')
echo $window
tempvar0="/"
tempvar1=${window%%/*}
tempvar2=${window#*/}
resultwindow=$tempvar1$tempvar0$tempvar1$tempvar2
echo $resultwindow
