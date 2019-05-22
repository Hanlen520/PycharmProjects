#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Shengjie.Liu
# @Time    : 2019-05-21 12:21
# @File    : adsAutomate.py
# @Desc    : 

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import os

#连接设备
device = MonkeyRunner.waitForConnection(3, "CB512FCM14")
#应用包名和活动名
dialer = "com.sonymobile.android.dialer/com.android.dialer.app.DialtactsActivity" #电话
settings = "com.android.settings/com.android.settings.Settings" #设置
#截图存放地址
ss_path = '/Users/liushengjie/Downloads/adsAutomateSS'


#等待时间
def mr_sleep(s_time=1):
    MonkeyRunner.sleep(s_time)


#广告展示、点击跳转、退出
def ads_show_click_exit(ss_before="ads_1.png", ss_after="ads_2.png"):
    # 等待10秒
    MonkeyRunner.sleep(10)
    # 截图1
    image1 = device.takeSnapshot()
    image1.writeToFile(os.path.join(ss_path, ss_before), 'png')
    # 点击广告
    device.touch(606, 1000, "DOWN_AND_UP")
    MonkeyRunner.sleep(1)
    device.touch(606, 1000, "DOWN_AND_UP")
    MonkeyRunner.sleep(10)
    # 截图2
    image2 = device.takeSnapshot()
    image2.writeToFile(os.path.join(ss_path, ss_after), 'png')
    # 返回键退出
    for i in range(1, 10):
        device.press('KEYCODE_BACK', "DOWN_AND_UP")
        MonkeyRunner.sleep(1)


#挂断
def hangup():
    # 启动应用
    device.startActivity(dialer)
    MonkeyRunner.sleep(2)
    # 点击拨号按键
    device.touch(940, 1660, "DOWN_AND_UP")
    MonkeyRunner.sleep(1)
    # 输入号码
    device.touch(870, 1228, "DOWN_AND_UP")
    device.touch(234, 852, "DOWN_AND_UP")
    device.touch(234, 852, "DOWN_AND_UP")
    # 点击拨打按钮
    device.touch(535, 1646, "DOWN_AND_UP")
    MonkeyRunner.sleep(3)
    # 挂断
    device.touch(545, 1571, "DOWN_AND_UP")
    ads_show_click_exit("hangup_1.png", "hangup_2.png")


#home键
def home():
    # 点击home键
    device.press('KEYCODE_HOME', "DOWN_AND_UP")
    ads_show_click_exit("home_1.png", "home_2.png")


def wifi_change():
    # 启动应用
    device.startActivity(settings)
    mr_sleep(2)
    # 点击NetWork & Internet
    device.touch(610, 357, "DOWN_AND_UP")
    mr_sleep(1)
    # 关闭Wi-Fi
    device.touch(980, 352, "DOWN_AND_UP")
    mr_sleep(2)
    # 打开Wi-Fi
    device.touch(933, 348, "DOWN_AND_UP")
    ads_show_click_exit("wifi_1.png", "wifi_2.png")


def main():
    #重复五次触发广告
    for i in range(0, 5):
        home()
        hangup()
        wifi_change()


if __name__ == '__main__':
    main()
