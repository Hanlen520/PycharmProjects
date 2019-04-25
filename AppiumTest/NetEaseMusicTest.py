#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Shengjie.Liu
# @Time    : 2019-04-24 15:39
# @File    : NetEaseMusicTest.py
# @Desc    : 

import unittest
from appium import webdriver
from time import sleep


class SimpleNetEaseMusicTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] = 'CB512FCM14'
        desired_caps['appPackage'] = 'com.netease.cloudmusic'
        desired_caps['appActivity'] = 'com.netease.cloudmusic.activity.LoadingActivity'
        desired_caps['newCommandTimeout'] = 150
        desired_caps['noReset'] = True
        desired_caps['unicodeKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)

    def tearDown(self):
        self.driver.quit()


class SimpleNetEaseMusicCase(SimpleNetEaseMusicTest):
    #每日签到
    def test_Check(self):
        menu = self.driver.find_element_by_id("com.netease.cloudmusic:id/p3")
        menu.click()
        check = self.driver.find_element_by_id("com.netease.cloudmusic:id/ad7")
        if(check.text != "Checked in"):
            check.click()
        else:
            self.driver.get_screenshot_as_file('/Users/liushengjie/Downloads/checked.png')

    #验证已签到
    def test_Check_Assert(self):
        menu = self.driver.find_element_by_id("com.netease.cloudmusic:id/p3")
        menu.click()
        checkTitle = self.driver.find_element_by_id("com.netease.cloudmusic:id/ad7")
        self.assertEqual(checkTitle.text, "Checked in")

