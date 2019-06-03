#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Shengjie.Liu
# @Time    : 2019-06-03 14:47
# @File    : calculator_test.py
# @Desc    :

#导入unittest测试框架
import unittest
#导入appium客户端库
from appium import webdriver
#导入time模块
from time import sleep
#导入HtmlTestRunner
import HtmlTestRunner

class CalculatorTest(unittest.TestCase):
    # pass

    # 截图路径
    SCREEN_SHOT_PATH = "/Users/liushengjie/PycharmProjects/AppiumTest/share/"

    #SetUP，case运行前的环境初始化
    def setUp(self):
        # pass
        #字典变量，初始化配置，提供建立session的所有必要信息：http://appium.io/docs/en/writing-running-appium/caps/index.html
        desired_caps = {}
        #被测应用平台：iOS/Android
        desired_caps['platformName'] = 'Android'
        #被测应用平台版本：adb shell getprop ro.build.version.release
        desired_caps['platformVersion'] = '8.0.0'
        #测试设备名：adb devices
        desired_caps['deviceName'] = 'CB512FCM14'
        #被测应用包名
        desired_caps['appPackage'] = 'weightloss.constellation.education.tools'
        #被测应用启动时的活动名
        desired_caps['appActivity'] = 'com.weightloss.constellation.education.tools.SplashActivityAlias'
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

    #TearDown，case运行后的环境恢复
    def tearDown(self):
        # pass
        #退出driver，关闭被测应用所有的关联窗口
        self.driver.quit()

    #TestCase，测试用例1
    def test_case_1(self):
        pass

    def test_plus(self):
        #预期结果等于10
        result = "10"
        #通过ID找到7
        seven = self.driver.find_element_by_id("weightloss.constellation.education.tools:id/button_7")
        #通过ID找到3
        three = self.driver.find_element_by_id("weightloss.constellation.education.tools:id/button_3")
        #通过ID找到+
        plus = self.driver.find_element_by_id("weightloss.constellation.education.tools:id/button_plus")
        #通过ID找到=
        equal = self.driver.find_element_by_id("weightloss.constellation.education.tools:id/button_equal")
        #通过ID找到结果
        real_result = self.driver.find_element_by_id("weightloss.constellation.education.tools:id/display")
        #点击7
        seven.click()
        #点击+
        plus.click()
        #点击3
        three.click()
        #点击=
        equal.click()
        #断言结果是否相等
        self.assertEqual(real_result.text, result)
        #截图
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + "plus_result.png")


#程序入口
if __name__ == '__main__':
    #TestSuite，将所有测试用例载入suite
    suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTest)
    #TestRunner，运行测试用例
    # unittest.TextTestRunner(verbosity=2).run(suite)

    #运行case+输出报告
    runner = HtmlTestRunner.HTMLTestRunner(output='cc_report')
    runner.run(suite)
