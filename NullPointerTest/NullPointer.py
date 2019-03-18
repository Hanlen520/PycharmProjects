#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os,sys
import time
#import commands
import threading

PATH = sys.path[0]
#先判断设备是否连接
os.popen("adb wait-for-device") 

#判断包名


#遍历文件获得activities 的值
def CheckNullPoint():
#Mac 下开启 
#    f = open(PATH+ "/" + "activities.txt","r")  
#windows 下开启
    f = open(PATH+ "\\" + "activities.txt","r")
    for line in f.readlines():
#	print (line)
        os.popen("adb shell am start -n com.cootek.smartinputv5/" + line)
        print("adb shell am start -n com.com.cootek.smartinputv5/" + line)
        time.sleep(3)
    f.close()

def CatLog():
#Mac 下的命令行
#    os.popen("adb logcat >> ~/Desktop/TouchPal_nullpoint.log")
#windows 下的命令行
    os.popen("adb logcat >> D:\\1TouchPal_nullpoint.log")

t2 = threading.Thread(target=CatLog)
t1 = threading.Thread(target=CheckNullPoint)
t2.start()
t1.start()
t1.join()
#num = commands.getstatusoutput("ps aux|grep adb|grep logcat|awk '{print $2}'")
#os.popen("kill -9 %s"%num)
#t2.join()
#print (t1.isAlive())
#print (t2.isAlive())