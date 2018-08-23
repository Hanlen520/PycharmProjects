# -*- coding: UTF-8 -*-

import subprocess
import unittest
from time import sleep
from appium import webdriver
import HtmlTestRunner


class AbsWorkoutTest(unittest.TestCase):

    # 截图存储路径
    SCREEN_SHOT_PATH = '/Users/a140/Desktop/screenshot_absworkout/class_all/'
    SCREEN_SHOT_CLASS_LIST = '/Users/a140/Desktop/screenshot_absworkout/class/list/'
    SCREEN_SHOT_CLASS_DONE = '/Users/a140/Desktop/screenshot_absworkout/class/done/'
    SCREEN_SHOT_CLASS_EXIT = '/Users/a140/Desktop/screenshot_absworkout/class/exit/'
    SCREEN_SHOT_CLASS_PAUSE = '/Users/a140/Desktop/screenshot_absworkout/class/pause/'
    SCREEN_SHOT_CLASS_VIDEO = '/Users/a140/Desktop/screenshot_absworkout/class/video/'
    SCREEN_SHOT_CLASS_BUG = '/Users/a140/Desktop/screenshot_absworkout/class/bug/'
    SCREEN_SHOT_SETTING_BUG = '/Users/a140/Desktop/screenshot_absworkout/setting/bug/'
    SCREEN_SHOT_SETTING = '/Users/a140/Desktop/screenshot_absworkout/setting/'

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.1'
        desired_caps['deviceName'] = '03083025d0250909'
        desired_caps['appPackage'] = 'abs.workout.fitness.tabata.hiit.stomach'
        desired_caps['appActivity'] = 'cootek.sevenmins.sport.WelcomeActivityAlias'
        desired_caps['newCommandTimeout'] = 120
        desired_caps['noReset'] = True
        desired_caps['printPageSourceOnFindFailure'] = True
        desired_caps['unicodeKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)

    def tearDown(self):
        self.driver.quit()

    def swipeUp(self, t=500, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeUpToCla(self, t=1000, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeUpToTab(self, t=100, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeUpSlow(self, t=1000, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(self, t=500, n=1):
        '''向下滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipLeft(self, t=500, n=1):
        '''向左滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipRight(self, t=500, n=1):
        '''向右滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    # adb command
    def sh(self, command):
        with subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as f:
            print(f.stdout.read())

    # 切换tap页
    def switch_tap(self, tap_num):
        ll_tap = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/ll_tap")
        ll_tap[tap_num].click()
        sleep(2)

    # 获取bug截图
    def get_bug_screenshot(self, loop_num, class_name, count):
        if 7 <= loop_num <= 13:
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + class_name + '/' +
                                               'bug/stage2' + 'index' + str(count + 1) + '.png')
        elif 14 <= loop_num <= 20:
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + class_name + '/' +
                                               'bug/stage3' + 'index' + str(count + 1) + '.png')
        elif 21 <= loop_num <= 27:
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + class_name + '/' +
                                               'bug/stage4' + 'index' + str(count + 1) + '.png')
        else:
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + class_name + '/' +
                                               'bug/stage1' + 'index' + str(count + 1) + '.png')

    # 获取课程最后动作的截图
    def get_last_action_screenshot(self, loop_num, class_name, exercise_name, last_num):
        if 7 <= loop_num <= 13:
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + class_name + '/stage2/'
                                               + str(last_num) + exercise_name.text + '.png')
        elif 14 <= loop_num <= 20:
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + class_name + '/stage3/'
                                               + str(last_num) + exercise_name.text + '.png')
        elif 21 <= loop_num <= 27:
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + class_name + '/stage4/'
                                               + str(last_num) + exercise_name.text + '.png')
        else:
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + class_name + '/stage1/'
                                               + str(last_num) + exercise_name.text + '.png')

    # 获取课程动作截图
    def get_action_screenshot(self, loop_num, class_name, exercise_name, count):
        if 7 <= loop_num <= 13:
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + class_name + '/stage2/'
                                               + str(count + 1) + exercise_name.text + '.png')
        elif 14 <= loop_num <= 20:
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + class_name + '/stage3/'
                                               + str(count + 1) + exercise_name.text + '.png')
        elif 21 <= loop_num <= 27:
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + class_name + '/stage4/'
                                               + str(count + 1) + exercise_name.text + '.png')
        else:
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_PATH + class_name + '/stage1/'
                                               + str(count + 1) + exercise_name.text + '.png')

    # 课程学习-课程视频页-进入课程classic
    def enter_class_video_classic(self):
        self.swipeUpToCla()
        enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
        enter_classic.click()
        sleep(2)
        button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
        button_go.click()
        sleep(2)
        button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
        button_go2.click()
        sleep(2)

    # 遍历课程classic
    def test_class_classic(self):
        self.swipeUpToCla()
        enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
        enter_classic.click()
        sleep(2)
        title_text = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/title_tv")
        self.assertEqual(title_text.text, "CLASSIC", "进入classic课程错误")
        loop_num = 0
        while loop_num < 28:
            button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
            button_go.click()
            sleep(2)
            button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
            button_go2.click()
            sleep(2)
            count = 0
            while count < 13:
                # noinspection PyBroadException
                try:
                    global exercise_name
                    exercise_name = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/"
                                                                   "exercise_name")
                    self.get_action_screenshot(loop_num, 'classic', exercise_name, count)
                except:
                    self.get_bug_screenshot(loop_num, 'classic', count)
                    button_ok = self.driver.find_element_by_id("android:id/button1")
                    button_ok.click()
                    sleep(1)
                button_next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_next")
                button_next.click()
                sleep(2)
                count = count + 1
            self.get_last_action_screenshot(loop_num, 'classic', exercise_name, 14)
            sleep(40)
            # noinspection PyBroadException
            try:
                button_cancel = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_cancel")
                button_cancel.click()
            except:
                pass
            sleep(2)
            self.sh('adb shell input keyevent 4')
            sleep(2)
            loop_num = loop_num + 1

    # 遍历课程hiit
    def test_class_hiit(self):
        self.swipeUp()
        enter_hiit = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
        enter_hiit[1].click()
        sleep(2)
        title_text = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/title_tv")
        self.assertEqual(title_text.text, "HIIT", "进入hiit课程错误")
        loop_num = 0
        while loop_num < 28:
            button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
            button_go.click()
            sleep(2)
            button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
            button_go2.click()
            sleep(2)
            count = 0
            while count < 13:
                # noinspection PyBroadException
                try:
                    global exercise_name
                    exercise_name = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/"
                                                                   "exercise_name")
                    self.get_action_screenshot(loop_num, 'hiit', exercise_name, count)
                except:
                    self.get_bug_screenshot(loop_num, 'hiit', count)
                    button_ok = self.driver.find_element_by_id("android:id/button1")
                    button_ok.click()
                    sleep(1)
                button_next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_next")
                button_next.click()
                sleep(2)
                count = count + 1
            self.get_last_action_screenshot(loop_num, 'hiit', exercise_name, 14)
            sleep(40)
            # noinspection PyBroadException
            try:
                button_cancel = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_cancel")
                button_cancel.click()
            except:
                pass
            sleep(2)
            self.sh('adb shell input keyevent 4')
            sleep(2)
            loop_num = loop_num + 1

    # 遍历课程tabata
    def test_class_tabata(self):
        self.swipeUpToTab()
        enter_tabata = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
        enter_tabata[1].click()
        sleep(2)
        title_text = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/title_tv")
        self.assertEqual(title_text.text, "TABATA", "进入tabata课程错误")
        loop_num = 0
        while loop_num < 28:
            button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
            button_go.click()
            sleep(2)
            button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
            button_go2.click()
            sleep(2)
            count = 0
            while count < 7:
                # noinspection PyBroadException
                try:
                    global exercise_name
                    exercise_name = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/"
                                                                   "exercise_name")
                    self.get_action_screenshot(loop_num, 'tabata', exercise_name, count)
                except:
                    self.get_bug_screenshot(loop_num, 'tabata', count)
                    button_ok = self.driver.find_element_by_id("android:id/button1")
                    button_ok.click()
                    sleep(1)
                button_next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_next")
                button_next.click()
                sleep(2)
                count = count + 1
            self.get_last_action_screenshot(loop_num, 'tabata', exercise_name, 8)
            sleep(40)
            # noinspection PyBroadException
            try:
                button_cancel = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_cancel")
                button_cancel.click()
            except:
                pass
            sleep(2)
            self.sh('adb shell input keyevent 4')
            sleep(2)
            loop_num = loop_num + 1

    # 课程学习-课程UI展示 --- 已废弃
    # def test_class_ui_classic(self):
    #     self.swipeUpToCla()
    #     enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     enter_classic.click()
    #     sleep(2)
    #     button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     button_go.click()
    #     sleep(2)
    #     # shoulders
    #     sleep(2)
    #     Shoulders = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Shoulders Stretch with Rotation")')
    #     Shoulders.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/shoulders.png')
    #     self.sh('adb shell input keyevent 4')
    #     # jump left
    #     sleep(2)
    #     jump = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Jump Left and Right")')
    #     jump.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/jump.png')
    #     self.sh('adb shell input keyevent 4')
    #     # reverse
    #     sleep(2)
    #     reverse = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Reverse Crunches")')
    #     reverse.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/reverse.png')
    #     self.sh('adb shell input keyevent 4')
    #     # plank
    #     sleep(2)
    #     plank = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Plank")')
    #     plank.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/plank.png')
    #     self.sh('adb shell input keyevent 4')
    #     # cat-cow
    #     sleep(2)
    #     cat = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Cat-Cow Stretch")')
    #     cat.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/cat.png')
    #     self.sh('adb shell input keyevent 4')
    #     sleep(2)
    #     # dead bug
    #     self.swipeUpSlow()
    #     sleep(2)
    #     dead_bug = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Dead Bug")')
    #     dead_bug.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/dead_bug.png')
    #     self.sh('adb shell input keyevent 4')
    #     # jumping jacks
    #     sleep(2)
    #     jumping_jacks = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Jumping Jacks")')
    #     jumping_jacks.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/jumping_jacks.png')
    #     self.sh('adb shell input keyevent 4')
    #     # plank
    #     sleep(2)
    #     plank_2 = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Plank")')
    #     plank_2.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/plant_2.png')
    #     self.sh('adb shell input keyevent 4')
    #     #########
    #     # dead bug
    #     sleep(2)
    #     self.swipeUpSlow()
    #     sleep(2)
    #     dead_bug_2 = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Dead Bug")')
    #     dead_bug_2.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/dead_bug_2.png')
    #     self.sh('adb shell input keyevent 4')
    #     # jumping jacks
    #     sleep(2)
    #     jumping_jacks_2 = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Jumping Jacks")')
    #     jumping_jacks_2.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/jumping_jacks_2.png')
    #     self.sh('adb shell input keyevent 4')
    #     # plank
    #     sleep(2)
    #     plank_3 = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Plank")')
    #     plank_3.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/plant_3.png')
    #     self.sh('adb shell input keyevent 4')
    #     # calf stretch left
    #     sleep(2)
    #     calf_left = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Calf Stretch Left")')
    #     calf_left.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/calf_left.png')
    #     self.sh('adb shell input keyevent 4')
    #     # calf stretch right
    #     sleep(2)
    #     calf_right = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Calf Stretch Right")')
    #     calf_right.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/calf_right.png')
    #     self.sh('adb shell input keyevent 4')
    #     ###
    #     sleep(2)
    #     self.swipeUp()
    #     sleep(2)
    #     back_stretch = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Back Stretch")')
    #     back_stretch.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/back_stretch.png')

    # 课程学习-课程列表页-点击"Go"
    def test_class_list_classic_go(self):
        self.enter_class_video_classic()
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_LIST + 'go.png')

    # 课程学习-课程列表页-点击动作预览
    def test_class_list_classic_preview(self):
        self.swipeUpToCla()
        enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
        enter_classic.click()
        sleep(2)
        title_text = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/title_tv")
        self.assertEqual(title_text.text, "CLASSIC", "进入classic课程错误")
        button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
        button_go.click()
        sleep(2)
        Shoulders = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("Shoulders Stretch with Rotation")')
        Shoulders.click()
        sleep(2)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_LIST + 'preview.png')

    # 课程学习-课程视频页-点击底部前后箭头
    def test_class_video_arrows(self):
        self.enter_class_video_classic()
        button_next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_next")
        button_next.click()
        sleep(1)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_VIDEO + 'arrows_two.png')
        button_back = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/turn_back")
        button_back.click()
        sleep(1)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_VIDEO + 'arrows_one.png')

    # 课程学习-课程视频页-点击暂停按钮
    def test_class_video_pause(self):
        self.enter_class_video_classic()
        pause = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/exercise_progress")
        pause.click()
        sleep(2)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_VIDEO + 'pause.png')

    # 课程学习-课程视频页-底部音符按钮
    def test_class_video_bgm(self):
        self.enter_class_video_classic()
        global bgm
        bgm = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/bgm_play_image")
        bgm.click()
        sleep(1)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_VIDEO + 'bgm_off.png')
        bgm.click()
        sleep(1)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_VIDEO + 'bgm_on.png')

    # 课程学习-课程视频页-扬声器按钮
    def test_class_video_sound(self):
        self.enter_class_video_classic()
        global sound
        sound = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/sound_play_image")
        sound.click()
        sleep(1)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_VIDEO + 'sound_off.png')
        sound.click()
        sleep(1)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_VIDEO + 'sound_on.png')

    # 课程学习-课程视频页-点击系统返回键/页面返回键
    def test_class_video_close(self):
        self.enter_class_video_classic()
        button_close = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_close")
        button_close.click()
        sleep(1)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_VIDEO + 'close.png')

    # 课程学习-动作暂停页
    def test_class_pause(self):
        self.test_class_video_pause()
        button_resume = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnResume")
        button_resume.click()
        sleep(2)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_PAUSE + 'resume.png')

    # 课程学习-退出运动弹框-关闭
    def test_class_exit_close(self):
        self.test_class_video_close()
        button_close = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_close")
        button_close.click()
        sleep(2)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_EXIT + 'close.png')

    # 课程学习-退出运动弹框-退出运动
    def test_class_exit_quit(self):
        self.test_class_video_close()
        button_quit = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnQuit")
        button_quit.click()
        sleep(2)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_EXIT + 'quit.png')

    # 课程学习-退出运动弹框-休息一会儿
    def test_class_exit_snooze(self):
        self.test_class_video_close()
        button_snooze = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnSnooze")
        button_snooze.click()
        sleep(2)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_EXIT + 'snooze.png')

    # 课程学习-运动完成页
    def test_class_done(self):
        self.enter_class_video_classic()
        count = 0
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_DONE + str(count) + '.png')
        while count < 13:
            button_next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_next")
            button_next.click()
            sleep(2)
            count = count + 1
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_DONE + str(count) + '.png')
        sleep(40)

    # 课程学习-运动完成页-添加/修改体重
    def test_class_done_weight(self):
        self.test_class_done()
        # 判断是否有弹窗，没有则pass
        try:
            button_cancel = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_cancel")
            button_cancel.click()
        except:
            pass
        current_weight = self.driver.find_element_by_id(
            "abs.workout.fitness.tabata.hiit.stomach:id/current_weight_tv")
        current_weight.click()
        edit_weight = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/edit_weight")
        edit_weight.clear()
        edit_weight.send_keys("70")
        edit_height = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/edit_height")
        edit_height.clear()
        edit_height.send_keys("180")
        button_save = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnSave")
        button_save.click()
        sleep(2)
        self.sh('adb shell input keyevent 4')
        sleep(2)
        self.sh('adb shell input keyevent 4')
        self.switch_tap(1)
        current_weight = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/currentWeight")
        current_height = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/currentHeight")
        try:
            self.assertIn('70', current_weight.text, '体重添加修改失败！')
        except Exception as msg:
            print(msg)
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_BUG + 'weight_error.png')
        try:
            self.assertIn('180', current_height.text, '身高添加修改失败！')
        except Exception as msg:
            print(msg)
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_BUG + 'height_error.png')

    # 课程学习-运动完成页-再来一次
    def test_class_done_again(self):
        self.test_class_done()
        # 判断是否有弹窗，没有则pass
        try:
            button_cancel = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_cancel")
            button_cancel.click()
        except:
            pass
        again = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Once again")')
        again.click()
        sleep(2)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_CLASS_DONE + 'again.png')

    # 课程学习-运动完成页-分享
    def test_class_done_share(self):
        pass

    # 分享
    def test_share(self):
        pass

    # 记录页
    def test_track(self):
        pass

    # 成就页
    def test_achievement(self):
        pass

    # 初次打开app
    def test_enter_choice_item(self):
        # 选择"TABATA"
        item_button = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/item_button")
        item_button[2].click()
        sleep(2)
        # 点击"NEXT"
        next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/next")
        next.click()
        sleep(2)
        # 默认时间"20:00"，点击进入app
        start = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_ok")
        start.click()

    # 设置页-去除广告
    def test_setting_ad(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        remove_ad = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/"
                                                   "setting_item_premium_entry")
        remove_ad.click()
        sleep(1)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_SETTING + 'after_click_remove_ad.png')
        # 点击关闭
        remove_ad_close = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/iv_close")
        remove_ad_close.click()

    # 设置页-添加提醒
    def test_setting_reminder_add(self):
        # 点击进入设置页
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        # 点击add reminder
        add_reminder = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/add_tag")
        add_reminder.click()
        # 点击reminder label
        reminder_label = self.driver.find_element_by_id(
            "abs.workout.fitness.tabata.hiit.stomach:id/reminder_program")
        reminder_label.click()
        # 选择"TABATA"
        label_list = self.driver.find_elements_by_class_name("android.widget.LinearLayout")
        label_list[2].click()
        # 重复提醒日期取消sunday
        repeat_day = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/day_check")
        repeat_day[0].click()
        # 点击"save"，提醒添加成功
        save = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnRight")
        save.click()
        sleep(2)
        # 断言提醒是否添加正确
        try:
            global reminder_text
            reminder_text = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/program_info")
            self.assertEqual(reminder_text.text, 'TABATA, Mon Tue Wed Thu Fri Sat', '添加提醒错误')
        except Exception as msg:
            print(msg)
            self.driver.get_screenshot_as_file(self.SCREEN_SHOT_SETTING_BUG + 'reminder_add_error.png')
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_SETTING + 'reminder_add.png')

    # 设置页-关闭提醒
    def test_setting_reminder_off(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        switch_reminder = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/switch_btn")
        switch_reminder[0].click()
        sleep(2)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_SETTING + 'reminder_off.png')

    # 设置页-打开提醒
    def test_setting_reminder_on(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        switch_reminder = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/switch_btn")
        switch_reminder[0].click()
        sleep(2)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_SETTING + 'reminder_on.png')

    # 设置页-删除提醒
    def test_setting_reminder_delete(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        reminder_list = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/program_info")
        reminder_list[0].click()
        sleep(2)
        self.swipeUp()
        button_delete = self.driver.find_element_by_id(
            "abs.workout.fitness.tabata.hiit.stomach:id/reminder_delete_btn")
        button_delete.click()
        sleep(2)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_SETTING + 'delete_done.png')

    # 设置页-修改提醒
    def test_setting_reminder_update(self):
        # 进入设置页
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        # 点击进入第一个提醒
        reminder_list = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/program_info")
        reminder_list[0].click()
        # 选择"HIIT"
        reminder_label = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/reminder_program")
        reminder_label.click()
        label_list = self.driver.find_elements_by_class_name("android.widget.LinearLayout")
        label_list[1].click()
        # 设置提醒时间为当前时间
        reminder_time = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/reminder_time")
        reminder_time.click()
        sleep(1)
        button_ok = self.driver.find_element_by_id("android:id/button1")
        button_ok.click()
        self.swipeUp()
        # 取消周三、周四、周五、周六的日期勾选
        repeat_day = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/day_check")
        repeat_day[3].click()
        repeat_day[4].click()
        repeat_day[5].click()
        repeat_day[6].click()
        # 保存提醒
        save = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnRight")
        save.click()
        sleep(2)
        # 断言提醒是否修改正确
        reminder_update_text = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/program_info")
        self.assertEqual(reminder_update_text.text, 'HIIT, Mon Tue ', '修改提醒错误')
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_SETTING + 'reminder_update.png')

    # 设置页-反馈意见
    def test_setting_feedback(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        self.swipeUp()
        sleep(2)
        feedback = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/feedback")
        feedback.click()
        sleep(2)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_SETTING + 'feedback.png')

    # 设置页-分享应用
    def test_setting_share(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        self.swipeUp()
        sleep(2)
        share = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/share")
        share.click()
        sleep(2)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_SETTING + 'share.png')

    # 设置页-隐私政策
    def test_setting_privacy(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        self.swipeUp()
        sleep(2)
        privacy = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/"
                                                 "view_setting_item_privacy_policy")
        privacy.click()
        sleep(2)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_SETTING + 'privacy.png')

    # 设置页-版本号
    def test_setting_version(self):
        version = "1.6.1"
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        self.swipeUp()
        sleep(2)
        version_text = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/version")
        self.assertEqual(version_text.text, version)
        self.driver.get_screenshot_as_file(self.SCREEN_SHOT_SETTING + 'version.png')


# run this test case after the first installation
# 设置页
def suite_setting():
    suite = unittest.TestSuite()
    suite.addTest(AbsWorkoutTest('test_enter_choice_item'))
    suite.addTest(AbsWorkoutTest('test_setting_reminder_add'))
    suite.addTest(AbsWorkoutTest('test_setting_reminder_delete'))
    suite.addTest(AbsWorkoutTest('test_setting_reminder_update'))
    suite.addTest(AbsWorkoutTest('test_setting_reminder_off'))
    suite.addTest(AbsWorkoutTest('test_setting_reminder_on'))
    suite.addTest(AbsWorkoutTest('test_setting_ad'))
    suite.addTest(AbsWorkoutTest('test_setting_feedback'))
    suite.addTest(AbsWorkoutTest('test_setting_share'))
    suite.addTest(AbsWorkoutTest('test_setting_privacy'))
    suite.addTest(AbsWorkoutTest('test_setting_version'))
    return suite


# run this test case after the suite_setting()
# 课程学习
def suite_class():
    suite = unittest.TestSuite()
    suite.addTest(AbsWorkoutTest('test_class_list_classic_go'))
    suite.addTest(AbsWorkoutTest('test_class_list_classic_preview'))
    suite.addTest(AbsWorkoutTest('test_class_video_arrows'))
    suite.addTest(AbsWorkoutTest('test_class_video_pause'))
    suite.addTest(AbsWorkoutTest('test_class_video_bgm'))
    suite.addTest(AbsWorkoutTest('test_class_video_sound'))
    suite.addTest(AbsWorkoutTest('test_class_video_close'))
    suite.addTest(AbsWorkoutTest('test_class_pause'))
    suite.addTest(AbsWorkoutTest('test_class_exit_close'))
    suite.addTest(AbsWorkoutTest('test_class_exit_quit'))
    suite.addTest(AbsWorkoutTest('test_class_exit_snooze'))
    suite.addTest(AbsWorkoutTest('test_class_done'))
    suite.addTest(AbsWorkoutTest('test_class_done_weight'))
    suite.addTest(AbsWorkoutTest('test_class_done_again'))
    suite.addTest(AbsWorkoutTest('test_class_done_share'))
    return suite


# run this test case in the end
# 遍历所有课程
def suite_class_all():
    suite = unittest.TestSuite()
    suite.addTest(AbsWorkoutTest('test_class_classic'))
    suite.addTest(AbsWorkoutTest('test_class_hiit'))
    suite.addTest(AbsWorkoutTest('test_class_tabata'))
    return suite


if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(output='report_absworkout')
    runner.run(suite_setting())
