#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Shengjie.Liu
# @Time    : 2019-04-25 10:25
# @File    : UiHelper.py
# @Desc    : Appium 方法封装类


import unittest
from appium import webdriver
import logging
from time import sleep

class UiHelper(unittest.TestCase):
    #Appium 连接建立和断开的封装
    # remoteHost = ""
    def __init__(self, configPath):
        remoteHost = ""
        self.desired_caps = {}
        self._driver = None
        file_object = open(configPath)
        try:
            for line in file_object:
                #'#'的行为注释，忽略
                if(line.startswith("#")):
                    continue
                line = line.strip()
                words = line.split("=")
                if(len(line) != 2):
                    continue
                if(words[0] == 'app'):
                    self.desired_caps[words[0]] = words[1]
                elif(words[0] == 'remoteHost'):
                    remoteHost = words[1]
                else:
                    self.desired_caps[words[0]] = words[1]
        finally:
            file_object.close()

    def initDriver(self):
        self_driver = webdriver.Remote(self.remoteHost, self.desired_caps)

    def quitDriver(self):
        if(self._driver):
            self._driver.quit()

    #控件查找方法的封装
    def findElement(self, controlInfo):
        element = ""
        if(controlInfo.startswith("//")):
            element = self._driver.find_element_by_xpath(controlInfo)
        elif(":id/" in controlInfo or ":string/" in controlInfo):
            element = self._driver.find_element_by_id(controlInfo)
        else:
            try:
                element = self._driver.find_element_by_name(controlInfo)
            except:
                logging.debug("Cannot find the element by id, try class name")
                element = self._driver.find_element_by_class_name(controlInfo)
        return element

    def findElementInParentElement(self, parentElement, childElementInfo):
        element = ""
        if(childElementInfo.startswith("//")):
            element = parentElement.find_element_by_xpath(childElementInfo)
        elif(":id/" in childElementInfo or ":string/" in childElementInfo):
            element = parentElement.find_element_by_id(childElementInfo)
        else:
            try:
                element = parentElement.find_element_by_name(childElementInfo)
            except:
                element = parentElement.find_element_by_class_name(childElementInfo)
        return element

    #UI等待方法的封装
    def waitForElement(self, elementInfo, period):
        for i in range(period):
            sleep(1)
            try:
                self.findElement(elementInfo)
                return
            except:
                continue
        raise Exception("Cannot find %s in %d seconds" % (elementInfo, period))

    #控件信息验证方法的封装
    def checkElementIsEnabled(self, elementInfo):
        element = self.findElement(elementInfo)
        return element.get_attribute("enabled")

    #to-do:
    #1.checkElementIsShown
    #2.checkElementShownInParentElement
    #3.checkElementIsSelected
    #4.checkElementIsChecked


