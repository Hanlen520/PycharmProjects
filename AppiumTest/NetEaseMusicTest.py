#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Shengjie.Liu
# @Time    : 2019-04-24 15:39
# @File    : NetEaseMusicTest.py
# @Desc    : 

import unittest
from appium import webdriver
from time import sleep
from UiHelper import UiHelper


class SimpleNetEaseMusicTest(unittest.TestCase):
    uiHelper = UiHelper(configPath="deviceConfig.txt")
    def setUp(self):
        # uiHelper = UiHelper()
        # to-do:创建初始条件，封装成方法调用
        try:
            uiHelper.initDriver()
        except:
            uiHelper.quitDriver()

    def tearDown(self):
        # uiHelper = UiHelper()
        # to-do:case结束后还原操作
        try:
            uiHelper.quitDriver()
            sleep(5)
        except:
            pass


class SimpleNetEaseMusicCase(SimpleNetEaseMusicTest):
    # to-do:1、填写账号密码进入应用2、点击获取积分
    pass
