#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Shengjie.Liu
# @Time    : 2019-05-31 14:45
# @File    : share2.py
# @Desc    : 报告展示+方法示例



#导入各种类库和包
import sys
import os
#导入unittest测试框架
import unittest
#导入appium客户端库
from appium import webdriver
from time import sleep

import HtmlTestRunner
import time

from appium.webdriver.common.touch_action import TouchAction


#创建测试类
class share2(unittest.TestCase):

    # 截图路径
    SCREEN_SHOT_PATH = "/Users/liushengjie/PycharmProjects/AppiumTest/share/"

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

    #封装方法：向上滑动
    def swipeUp(self, t=500, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    #封装方法：截图
    def get_screenshot(self, ss_name):
        timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + ss_name + timestamp + '.png')

    #测试用例1：True
    def test_case1(self):
        a = 2
        b = 3
        self.assertNotEqual(a, b)

    #测试用例2：True
    def test_case2(self):
        pass

    #测试用例3：False
    def test_case3(self):
        a = 2
        b = 3
        self.assertEqual(a, b)

    #点击
    def test_click(self):
        try:
            a = self.driver.find_element_by_id("com.netease.cloudmusic:id/anm")
            b = a.find_element_by_class_name("android.widget.LinearLayout")
            c = b.find_elements_by_class_name("android.widget.FrameLayout")
            d = c[1].find_element_by_class_name("android.widget.TextView")
            d.click()
        except:
             self.get_screenshot("click_fail")
        sleep(2)
        self.get_screenshot("click")

    #长按
    def test_long_click(self):
        try:
            a = self.driver.find_element_by_id("com.netease.cloudmusic:id/anm")
            b = a.find_element_by_class_name("android.widget.LinearLayout")
            c = b.find_elements_by_class_name("android.widget.FrameLayout")
            d = c[1].find_element_by_class_name("android.widget.TextView")
            actions = TouchAction(self.driver)
            actions.long_press(d)
            actions.perform()
        except:
             self.get_screenshot("long_click_fail")
        sleep(2)
        self.get_screenshot("long_click")


    #back键
    def test_back_key(self):
        self.get_screenshot("before_click")
        try:
            a = self.driver.find_element_by_id("com.netease.cloudmusic:id/anm")
            b = a.find_element_by_class_name("android.widget.LinearLayout")
            c = b.find_elements_by_class_name("android.widget.FrameLayout")
            d = c[1].find_element_by_class_name("android.widget.TextView")
            d.click()
        except:
             self.get_screenshot("back_fail")
        sleep(2)
        self.get_screenshot("after_click")
        self.driver.keyevent(4)
        sleep(2)
        self.get_screenshot("after_back")






if __name__ == '__main__':
    #TestSuite
    suite = unittest.TestLoader().loadTestsFromTestCase(share2)
    #TestRunner
    # unittest.TextTestRunner(verbosity=2).run(suite)

    #运行case+输出报告
    runner = HtmlTestRunner.HTMLTestRunner(output='my_report')
    runner.run(suite)
