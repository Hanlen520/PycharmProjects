#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Shengjie.Liu
# @Time    : 2019-05-31 12:05
# @File    : share1.py
# @Desc    : 两个例子


#导入各种类库和包
import sys
import os
#导入unittest测试框架
import unittest
#导入appium客户端库
from appium import webdriver
from time import sleep
import time

#创建测试类
class share1(unittest.TestCase):

    #截图路径
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
        #启动应用时等待10秒，跳过广告页面
        sleep(10)

    #case运行后的环境恢复
    def tearDown(self):
        self.driver.quit()

    #测试用例1
    # def test_case1(self):
    #     pass

    def swipeUp(self, t=500, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    #截图的方法封装
    def get_screenshot(self, ss_name):
        timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + ss_name + timestamp + '.png')

    #登录网易云音乐
    @unittest.skip("skip test_login")
    def test_login(self):
        dr = u"每日推荐"
        #登录页面-邮箱
        mailButton = self.driver.find_element_by_id("com.netease.cloudmusic:id/ajw")
        mailButton.click()
        #登录页面-账号输入框
        accountText = self.driver.find_element_by_id("com.netease.cloudmusic:id/il")
        accountText.send_keys("L767096730@163.com")
        #登录页面-密码输入框
        passwordText = self.driver.find_element_by_id("com.netease.cloudmusic:id/im")
        passwordText.send_keys("Meet163@3.14")
        sleep(2)
        #登录页面-登录按钮
        loginButton = self.driver.find_element_by_id("com.netease.cloudmusic:id/os")
        loginButton.click()
        sleep(2)
        #根据登录后主页中的"每日推荐"字段判断是否登录成功
        try:
            a = self.driver.find_element_by_id("com.netease.cloudmusic:id/anm")
            b = a.find_element_by_class_name("android.widget.LinearLayout")
            c = b.find_elements_by_class_name("android.widget.FrameLayout")
            d = c[0].find_element_by_class_name("android.widget.TextView")
            sleep(2)
            self.assertEqual(d.text, dr)
        except:
            #未找到"每日推荐"字段时，截图保存出错界面的信息
            timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + 'login_fail' + timestamp + '.png')
        #截图
        timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + 'login_success' + timestamp + '.png')


    #退出账号
    # @unittest.skip("skip test_logout")
    def test_logout(self):
        register_text = u"Register"
        try:
            #主页-左上角-侧滑菜单栏
            self.driver.find_element_by_id("com.netease.cloudmusic:id/p3").click()
        except:
            #back 键退出升级提醒的窗口
            self.driver.press_keycode(4)
            sleep(2)
            #主页-左上角-侧滑菜单栏
            self.driver.find_element_by_id("com.netease.cloudmusic:id/p3").click()
        try:
            #侧滑菜单页面-settings按钮
            self.driver.find_element_by_id("com.netease.cloudmusic:id/b_w").click()
        except:
            #back 键退出升级提醒的窗口
            self.driver.press_keycode(4)
            sleep(2)
            #侧滑菜单页面-settings按钮
            self.driver.find_element_by_id("com.netease.cloudmusic:id/b_w").click()
        sleep(2)
        #向上滑动
        for i in range(0, 3):
            self.swipeUp()
            sleep(1)
        #Settings页面-Change ID按钮
        self.driver.find_element_by_id("com.netease.cloudmusic:id/y2").click()
        sleep(1)
        #Settings页面-是否退出的Toast-Quit按钮
        self.driver.find_element_by_id("com.netease.cloudmusic:id/bcf").click()
        sleep(2)
        #登录页面-注册
        register = self.driver.find_element_by_id("com.netease.cloudmusic:id/ams")
        #根据退出账号后的登录页面中的"Register"字段判断是否登出成功
        self.assertEqual(register.text, register_text)
        #截图
        # timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
        # self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + 'logout_success' + timestamp + '.png')
        #调用封装的截图方法
        self.get_screenshot("logout_success")


if __name__ == '__main__':
    #TestSuite
    suite = unittest.TestLoader().loadTestsFromTestCase(share1)
    #TestRunner
    unittest.TextTestRunner(verbosity=2).run(suite)
