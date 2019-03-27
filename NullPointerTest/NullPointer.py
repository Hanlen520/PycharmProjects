#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
import sys
import time
import threading

PATH = sys.path[0]
PKG_NAME = sys.argv[1]

# 先判断设备是否连接
os.popen("adb wait-for-device")


# 遍历文件获得activities 的值
def CheckNullPoint():
    f = open(PATH + "/" + "AC_list_filter", "r")
    for line in f.readlines():
        os.popen('adb shell am start -n %s/%s' % (PKG_NAME, line))
        # print("adb shell am start -n %s/%s" % (PKG_NAME, line))
    time.sleep(3)
    f.close()


def CatLog():
    os.popen('adb logcat >> %s/log.txt' % PATH)


def kill_adb():
    os.popen('adb kill-server')


def quit_app():
    os.popen('adb shell input keyevent 4')


def clear_log():
    os.popen('adb logcat -c')

# 清空历史log
clear_log()
# t2 = threading.Thread(target=CatLog)
# t1 = threading.Thread(target=CheckNullPoint)
# t2.start()
# t1.start()
# t1.join()
CheckNullPoint()
print "Success"
# back键退出应用
for i in range(10):
    quit_app()

# kill_adb()
