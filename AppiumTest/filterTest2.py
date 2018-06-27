import subprocess
import unittest
from time import sleep
from appium import webdriver
from uiHelper import UiHelper

class filterTest(unittest.TestCase):

    def test_enterFilter(self):
        uiHelper = UiHelper("/Users/a140/PycharmProjects/AppiumTest/deviceConfig")
        uiHelper.initDriver()
        sleep(10)
        print("滑动欢迎页进入app")
        # 向左滑动跳过引导页
        x = 0
        while x < 3:
            #self.swipeLeft()
            uiHelper.swipeLeft()
            x += 1
        #enter_app = self.driver.find_element_by_id("com.eyefilter.night:id/enter")
        enter_app = uiHelper.findElement("com.eyefilter.night:id/enter")
        enter_app.click()
        self.filter()


    #开启关闭护目镜/调整护目镜颜色
    def filter(self):
        filter_switch = UiHelper.findElement(self, "com.eyefilter.night:id/mSwitch")
        print("开启护目镜")
        filter_switch.click()
        #self.driver.implicitly_wait(3)
        sleep(3)
        #self.driver.save_screenshot("filter_on.png")
        UiHelper.saveScreenshot(UiHelper, "/Users/a140/Downloads/filter_on.png")

        #self.driver.implicitly_wait(3)
        try:
            print("关闭护目镜")
            filter_switch.click()
            print("开启Auto Enable")
            #enable = self.driver.find_element_by_id("android:id/button1")
            enable = UiHelper.findElement("android:id/button1")
            enable.click()
            #self.driver.implicitly_wait(3)
            sleep(4)
            #self.driver.save_screenshot("auto_enable_on.png")
            UiHelper.saveScreenshot(UiHelper, "/Users/a140/Downloads/auto_enable_on.png")
        except:
            pass
        #self.driver.implicitly_wait(10)
        #color1 = self.driver.find_element_by_id("com.eyefilter.night:id/change_color1")
        color1 = UiHelper.waitForElement(UiHelper, "com.eyefilter.night:id/change_color1", 10)
        color1.click()
        sleep(2)
        #self.driver.save_screenshot("filter_color1.png")
        UiHelper.saveScreenshot(UiHelper, "/Users/a140/Downloads/filter_color1.png")
        # self.driver.implicitly_wait(10)
        # color2 = self.driver.find_element_by_id("com.eyefilter.night:id/change_color2")
        # color2.click()
        # sleep(2)
        # self.driver.save_screenshot("filter_color2.png")
        # self.driver.implicitly_wait(10)
        # color3 = self.driver.find_element_by_id("com.eyefilter.night:id/change_color3")
        # color3.click()
        # sleep(2)
        # self.driver.save_screenshot("filter_color3.png")
        # self.driver.implicitly_wait(10)
        # color4 = self.driver.find_element_by_id("com.eyefilter.night:id/change_color4")
        # color4.click()
        # sleep(2)
        # self.driver.save_screenshot("filter_color4.png")
        # color5 = self.driver.find_element_by_id("com.eyefilter.night:id/change_color5")
        # color5.click()
        # sleep(3)
        # self.driver.save_screenshot("filter_color5.png")
        # self.sh('adb shell input keyevent 4')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(filterTest)
    unittest.TextTestRunner(verbosity=2).run(suite)