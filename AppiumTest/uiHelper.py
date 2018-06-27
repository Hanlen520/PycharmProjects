import sys
import os
from appium import webdriver
from time import sleep
from enum import Enum
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class UiHelper:
    remoteHost = "http://127.0.0.1:4723/wd/hub"
    def __init__(self, configPath):
        self.desired_caps = {}
        self._driver = None
        file_object = open(configPath)
        try:
            for line in file_object:
                if (line.startswith("#")):
                    continue

                line = line.strip()
                words = line.split("=")
                if (len(words) != 2):
                    continue

                if (words[0] == 'app'):
                    self.desired_caps[words[0]] = PATH(words[1])
                elif (words[0] == 'remoteHost'):
                    remoteHost = words[1]
                else:
                    self.desired_caps[words[0]] = words[1]
        finally:
            file_object.close()

    def initDriver(self):
        self._driver = webdriver.Remote(self.remoteHost, self.desired_caps)

    def quitDriver(self):
        if (self._driver):
            self._driver.quit()

    def findElement(self, controlInfo):
        element = ""
        if(controlInfo.startswith("//")):
            element = self._driver.find_element_by_xpath(controlInfo)
        elif(":id/" in controlInfo or ":string/" in controlInfo):
            element = self._driver.find_element_by_id(controlInfo)
        else:
            #剩下的字符串没有特点，无法区分，因此先尝试通过名称查找
            try:
                element = self._driver.find_element_by_name(controlInfo)
            except:
                #如果通过名称不能找到则通过class name查找
                element = self._driver.find_element_by_class_name(controlInfo)

        return element

    #获取屏幕宽度和高度
    def getSize(self):
        x = self._driver.get_window_size()['width']
        y = self._driver.get_window_size()['height']
        return (x, y)

    #滑动
    def swipe(self, x1, y1, x2, y2):
        self._driver.swipe(x1, y1, x2, y2)

    #向左滑动跳过引导页，进入app
    def swipeLeft(self):
        l = self.getSize()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1, y1, x2, y1)

    def saveScreenshot(self, pathOnPC):
        self._driver.save_screenshot(pathOnPC)

    def waitForElement(self, elementInfo, period):
        for i in range (0, period):
            sleep(1)
            try:
                self.findElement(elementInfo)
                return
            except:
                continue

        raise Exception("Cannot find %s in %d seconds" %(elementInfo,period))





