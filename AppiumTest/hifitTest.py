# -*- coding: UTF-8 -*-
__author__ = 'Shengjie.Liu'


import subprocess
import unittest
from time import sleep
from appium import webdriver
import HtmlTestRunner
import os


class HifitTest(unittest.TestCase):

    # 截图存放路径
    SCREEN_SHOT_PATH = '/Users/a140/Desktop/screenshot_hifit/'
    # 其他截图存放路径
    SCREEN_SHOT_PATH_OTHERS = '/Users/a140/Desktop/screenshot_hifit/screenshot_others/'
    # apk文件存放路径
    # APK_PATH = ' /Users/a140/Desktop/hifit_latest_10/'
    PATH = '/Users/a140/Desktop/hifit_latest_10/'

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.1'
        desired_caps['deviceName'] = '03083025d0250909'
        desired_caps['appPackage'] = 'hifit.workout.butt.fitness.weightloss'
        desired_caps['appActivity'] = 'cootek.sevenmins.sport.activity.WelcomeActivity'
        desired_caps['newCommandTimeout'] = 120
        desired_caps['noReset'] = True
        desired_caps['printPageSourceOnFindFailure'] = True
        desired_caps['unicodeKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)

    def tearDown(self):
        self.driver.quit()

    # 向上滑动屏幕，查看底部feeds
    def swipeUp(self, t=250):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 滑动到首页底部
    def switch2fc(self):
        count = 0
        while count < 4:
            self.swipeUp()
            sleep(2)
            count += 1

    # 测试用
    def test_switch2fc(self):
        sleep(5)
        count = 0
        while count < 4:
            self.swipeUp()
            sleep(2)
            count += 1
        sleep(5)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + 'testfcfc.png')

    # adb command
    def sh(self, command):
        with subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as f:
            print(f.stdout.read())

    # 获取feeds截图
    def get_screenshots(self, apkname):
        sleep(5)
        self.switch2fc()
        sleep(5)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + apkname + "FC.png")
        sleep(2)
        self.switchTap()
        sleep(5)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + apkname + "Discover.png")

    # 进入app
    def test_enter(self, apkname='hifit'):
        try:
            self.enter_version1(apkname)
            if self.enter_version3(apkname) is True:
                pass
            else:
                self.get_screenshots(apkname)
        except:
            try:
                self.enter_version3(apkname)
                pass
            except:
                try:
                    self.enter_version2(apkname)
                    self.get_screenshots(apkname)
                except:
                    try:
                        self.enter_version4()
                        self.get_screenshots(apkname)
                    except:
                        try:
                            self.enter_version5(apkname)
                            self.get_screenshots(apkname)
                        except:
                            try:
                                self.get_screenshots(apkname)
                            except:
                                pass

    # v366，第一次进入app
    def enter_version1(self, apkname):
        gender = self.driver.find_element_by_id("hifit.workout.butt.fitness.weightloss:id/iv_female")
        gender.click()
        try:
            iv_lose_fat = self.driver.find_element_by_id("hifit.workout.butt.fitness.weightloss:id/lose_fat_tv")
            iv_lose_fat.click()
        except:
            pass
        btn_start = self.driver.find_element_by_id("hifit.workout.butt.fitness.weightloss:id/btn_start")
        btn_start.click()
        sleep(5)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH_OTHERS + apkname + 'enter_version1.png')

    # 进入时，隐私协议+性别运动类型选择
    def enter_version2(self, apkname):
        btn_accept = self.driver.find_element_by_id(
            "hifit.workout.butt.fitness.weightloss:id/privacy_policy_guide_agree_btn")
        btn_accept.click()
        iv_female = self.driver.find_element_by_id("hifit.workout.butt.fitness.weightloss:id/iv_female")
        iv_female.click()
        iv_lose_fat = self.driver.find_element_by_id("hifit.workout.butt.fitness.weightloss:id/lose_fat_tv")
        iv_lose_fat.click()
        btn_start = self.driver.find_element_by_id("hifit.workout.butt.fitness.weightloss:id/btn_start")
        btn_start.click()
        sleep(2)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH_OTHERS + apkname + 'enter_version2.png')

    # 成功进入应用，提醒升级到新版本
    def enter_version3(self, apkname):
        update_text = self.driver.find_element_by_id("hifit.workout.butt.fitness.weightloss:id/title")
        self.assertEqual(update_text.text, "New Version Found!")
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH_OTHERS + apkname + 'noticeUpdate.png')
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH_OTHERS + apkname + "enter_version3.png")

    # 进入时，弹出隐私协议
    def enter_version4(self):
        btn_accept = self.driver.find_element_by_id(
            "hifit.workout.butt.fitness.weightloss:id/privacy_policy_guide_agree_btn")
        btn_accept.click()

    # 进入时，性别运动类型选择
    def enter_version5(self, apkname):
        iv_female = self.driver.find_element_by_id("hifit.workout.butt.fitness.weightloss:id/iv_female")
        iv_female.click()
        iv_lose_fat = self.driver.find_element_by_id("hifit.workout.butt.fitness.weightloss:id/lose_fat_tv")
        iv_lose_fat.click()
        btn_start = self.driver.find_element_by_id("hifit.workout.butt.fitness.weightloss:id/btn_start")
        btn_start.click()
        sleep(2)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH_OTHERS + apkname + 'enter_version5.png')

    # 切换到discovery
    def switchTap(self):
        btn_tap = self.driver.find_element_by_id("hifit.workout.butt.fitness.weightloss:id/sm_bottom_indicator_iv3")
        btn_tap.click()
        sleep(5)

    # 升级版本
    def updateVersion(self, apk_name):
        self.sh('adb install -r' + ' ' + self.PATH + apk_name)
        sleep(45)

    # 获取apk名字
    def listApk(self):
        file_list = []
        files = os.listdir(self.PATH)
        for file in files:
            if file[0] == '.':
                pass
            else:
                file_list.append(file)
        file_list.sort()
        return file_list

    # 连续升级至新版本，获取截图
    def test_update(self):
        apks = self.listApk()
        # print(apks)
        for apk_name in apks:
            if apk_name != apks[0]:
                self.updateVersion(apk_name)
                print(apk_name + ' ' + 'Successful installation')
                self.setUp()
                self.test_enter(apk_name)


def suite_test():
    suite = unittest.TestSuite()
    suite.addTest(HifitTest('test_enter'))
    suite.addTest(HifitTest('test_update'))
    # suite.addTest(HifitTest('test_switch2fc'))
    return suite


if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(output='report_hifit')
    runner.run(suite_test())
