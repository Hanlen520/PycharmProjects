#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Shengjie.Liu
# @Time    : 2019-05-29 18:19
# @File    : share.py
# @Desc    : 基础框架

#导入各种类库和包
import sys
import os
#导入unittest测试框架
import unittest
#导入appium客户端库
from appium import webdriver
from time import sleep

#创建测试类
class share(unittest.TestCase):
    #case运行前的环境初始化
    def setUp(self):
        #字典变量，初始化配置，提供建立session的所有必要信息：http://appium.io/docs/en/writing-running-appium/caps/index.html
        desired_caps = {}
        #被测应用平台：iOS/Android
        desired_caps['platformName'] = 'Android'
        #被测应用平台版本：adb shell getprop ro.build.version.release
        desired_caps['platformVersion'] = '8.0.0'
        #测试设备名：adb devices
        desired_caps['deviceName'] = 'CB512FCM14'
        #被测应用包名
        desired_caps['appPackage'] = 'com.netease.cloudmusic'
        #被测应用启动时的活动名
        desired_caps['appActivity'] = 'com.netease.cloudmusic.activity.LoadingActivity'
        # desired_caps['appActivity'] = "com.netease.cloudmusic.activity.LoginActivity"
        #服务端等待客户端发送消息的超时时间
        desired_caps['newCommandTimeout'] = 150
        #在一个session开始前不重置被测程序的状态
        desired_caps['noReset'] = True
        #是否支持uicode的键盘（输入中文需设置）
        desired_caps['unicodeKeyboard'] = True
        #以desired_caps作为参数初始化WebDriver连接
        #Appium服务器的IP：http://localhost
        #端口号：4723
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)

    #case运行后的环境恢复
    def tearDown(self):
        self.driver.quit()

    #测试用例1
    def test_case1(self):
        pass


if __name__ == '__main__':
    #TestSuite
    suite = unittest.TestLoader().loadTestsFromTestCase(share)
    #TestRunner
    unittest.TextTestRunner(verbosity=2).run(suite)
