import subprocess
import unittest
from time import sleep
from appium import webdriver


class AbsWorkoutTest(unittest.TestCase):

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

    # 遍历课程classic
    # def test_class_classic(self):
    #     self.swipeUpToCla()
    #     enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     enter_classic.click()
    #     sleep(2)
    #     loop_num = 0
    #     while loop_num < 28:
    #         button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #         button_go.click()
    #         sleep(2)
    #         button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
    #         button_go2.click()
    #         sleep(2)
    #         count = 0
    #         while count < 13:
    #             button_next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_next")
    #             button_next.click()
    #             sleep(2)
    #             count = count + 1
    #         sleep(40)
    #         try:
    #             button_cancel = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_cancel")
    #             button_cancel.click()
    #         except:
    #             pass
    #         sleep(2)
    #         self.sh('adb shell input keyevent 4')
    #         sleep(2)
    #         self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/' + str(loop_num) +
    #                                            '.png')
    #         loop_num = loop_num + 1

    # def test_class_hiit(self):
    #     self.swipeUp()
    #     enter_hiit = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     enter_hiit[1].click()
    #     sleep(2)
    #     # self.driver.get_screenshot_as_file('/Users/a140/Desktop/hiit.png')
    #     loop_num = 0
    #     while loop_num < 28:
    #         button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #         button_go.click()
    #         sleep(2)
    #         button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
    #         button_go2.click()
    #         sleep(2)
    #         count = 0
    #         while count < 13:
    #             # noinspection PyBroadException
    #             try:
    #                 exercise_name = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/"
    #                                                                "exercise_name")
    #                 if 7 <= loop_num <= 13:
    #                     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/hiit/stage2/' +
    #                                                        str(count) + exercise_name.text + '.png')
    #                 elif 14 <= loop_num <= 20:
    #                     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/hiit/stage3/' +
    #                                                        str(count) + exercise_name.text + '.png')
    #                 elif 21 <= loop_num <= 27:
    #                     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/hiit/stage4/' +
    #                                                        str(count) + exercise_name.text + '.png')
    #                 else:
    #                     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/hiit/stage1/' +
    #                                                        str(count) + exercise_name.text + '.png')
    #             except:
    #                 self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/hiit/bug/'
    #                                                    + 'num' + str(loop_num + 1) + 'index' + str(count + 1) + '.png')
    #                 button_ok = self.driver.find_element_by_id("android:id/button1")
    #                 button_ok.click()
    #                 sleep(1)
    #                 self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/hiit/bug/'
    #                                                    + 'num' + str(loop_num + 1) + 'index' + str(count + 1) + '2.png')
    #             button_next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_next")
    #             button_next.click()
    #             sleep(2)
    #             count = count + 1
    #         if 7 <= loop_num <= 13:
    #             self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/hiit/stage2/' + '14' +
    #                                                exercise_name.text + '.png')
    #         elif 14 <= loop_num <= 20:
    #             self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/hiit/stage3/' + '14' +
    #                                                exercise_name.text + '.png')
    #         elif 21 <= loop_num <= 27:
    #             self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/hiit/stage4/' + '14' +
    #                                                exercise_name.text + '.png')
    #         else:
    #             self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/hiit/stage1/' + '14' +
    #                                                exercise_name.text + '.png')
    #         sleep(40)
    #         # noinspection PyBroadException
    #         try:
    #             button_cancel = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_cancel")
    #             button_cancel.click()
    #         except:
    #             pass
    #         sleep(2)
    #         self.sh('adb shell input keyevent 4')
    #         sleep(2)
    #         # self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/hiit/' + str(loop_num) +
    #         #                                    '.png')
    #         loop_num = loop_num + 1

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
            # noinspection PyBroadException
            try:
                button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
                button_go.click()
            except:
                self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/tabata/bug/button_go_error.png')
                pass
            sleep(2)
            try:
                button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
                button_go2.click()
            except:
                self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/tabata/bug/button_go2_error.png')
                pass
            sleep(2)
            count = 0
            while count < 7:
                # noinspection PyBroadException
                try:
                    exercise_name = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/"
                                                                   "exercise_name")
                    if 7 <= loop_num <= 13:
                        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/tabata/stage2/' +
                                                           str(count + 1) + exercise_name.text + '.png')
                    elif 14 <= loop_num <= 20:
                        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/tabata/stage3/' +
                                                           str(count + 1) + exercise_name.text + '.png')
                    elif 21 <= loop_num <= 27:
                        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/tabata/stage4/' +
                                                           str(count + 1) + exercise_name.text + '.png')
                    else:
                        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/tabata/stage1/' +
                                                           str(count + 1) + exercise_name.text + '.png')
                except:
                    if 7 <= loop_num <= 13:
                        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/tabata/bug/'
                                                           + 'stage2' + 'index' + str(count + 1) + '.png')
                    elif 14 <= loop_num <= 20:
                        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/tabata/bug/'
                                                           + 'stage3' + 'index' + str(count + 1) + '.png')
                    elif 21 <= loop_num <= 27:
                        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/tabata/bug/'
                                                           + 'stage4' + 'index' + str(count + 1) + '.png')
                    else:
                        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/tabata/bug/'
                                                           + 'stage1' + 'index' + str(count + 1) + '.png')
                    button_ok = self.driver.find_element_by_id("android:id/button1")
                    button_ok.click()
                    sleep(1)
                    self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/tabata/bug/'
                                                       + 'num' + str(loop_num + 1) + 'index' + str(count + 1) + '2.png')
                button_next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_next")
                button_next.click()
                sleep(2)
                count = count + 1
            if 7 <= loop_num <= 13:
                self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/tabata/stage2/' + '8' +
                                                   exercise_name.text + '.png')
            elif 14 <= loop_num <= 20:
                self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/tabata/stage3/' + '8' +
                                                   exercise_name.text + '.png')
            elif 21 <= loop_num <= 27:
                self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/tabata/stage4/' + '8' +
                                                   exercise_name.text + '.png')
            else:
                self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/tabata/stage1/' + '8' +
                                                   exercise_name.text + '.png')
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







    # 课程UI展示
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

    # # 课程UI展示
    # def test_class_ui(self):
    #     pass
    #
    # # 课程列表页，点击"Go"
    # def test_class_list_classic_go(self):
    #     self.swipeUpToCla()
    #     enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     enter_classic.click()
    #     sleep(2)
    #     button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     button_go.click()
    #     sleep(2)
    #     button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
    #     button_go2.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/list/go.png')
    #
    # # 课程列表页，点击动作预览
    # def test_class_list_classic_preview(self):
    #     self.swipeUpToCla()
    #     enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     enter_classic.click()
    #     sleep(2)
    #     button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     button_go.click()
    #     sleep(2)
    #     Shoulders = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Shoulders Stretch with Rotation")')
    #     Shoulders.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/list/preview.png')
    #
    # # 动作预览
    # def test_class_preview(self):
    #     pass
    #
    # # 课程视频
    # def test_class_video(self):
    #     pass
    #
    # # 点击底部前后箭头
    # def test_class_video_arrows(self):
    #     self.swipeUpToCla()
    #     enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     enter_classic.click()
    #     sleep(2)
    #     button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     button_go.click()
    #     sleep(2)
    #     button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
    #     button_go2.click()
    #     sleep(2)
    #     button_next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_next")
    #     button_next.click()
    #     sleep(1)
    #     button_next.click()
    #     sleep(1)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/video/arrows_two.png')
    #     button_back = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/turn_back")
    #     button_back.click()
    #     sleep(1)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/video/arrows_one.png')
    #
    # # 点击暂停按钮
    # def test_class_video_pause(self):
    #     self.swipeUpToCla()
    #     enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     enter_classic.click()
    #     sleep(2)
    #     button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     button_go.click()
    #     sleep(2)
    #     button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
    #     button_go2.click()
    #     sleep(2)
    #     pause = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/exercise_progress")
    #     pause.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/video/pause.png')
    #
    # # 底部音符按钮
    # def test_class_video_bgm(self):
    #     self.swipeUpToCla()
    #     enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     enter_classic.click()
    #     sleep(2)
    #     button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     button_go.click()
    #     sleep(2)
    #     button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
    #     button_go2.click()
    #     sleep(2)
    #     bgm = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/bgm_play_image")
    #     bgm.click()
    #     sleep(1)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/video/bgm_off.png')
    #     bgm.click()
    #     sleep(1)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/video/bgm_on.png')
    #
    # # 扬声器按钮
    # def test_class_video_sound(self):
    #     self.swipeUpToCla()
    #     enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     enter_classic.click()
    #     sleep(2)
    #     button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     button_go.click()
    #     sleep(2)
    #     button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
    #     button_go2.click()
    #     sleep(2)
    #     sound = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/sound_play_image")
    #     sound.click()
    #     sleep(1)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/video/sound_off.png')
    #     sound.click()
    #     sleep(1)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/video/sound_on.png')
    #
    # # 点击系统返回键/页面返回键
    # def test_class_video_close(self):
    #     self.swipeUpToCla()
    #     enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     enter_classic.click()
    #     sleep(2)
    #     button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     button_go.click()
    #     sleep(2)
    #     button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
    #     button_go2.click()
    #     sleep(2)
    #     button_close = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_close")
    #     button_close.click()
    #     sleep(1)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/video/close.png')
    #
    # # 动作暂停页
    # def test_class_pause(self):
    #     self.test_class_video_pause()
    #     button_resume = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnResume")
    #     button_resume.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/pause/resume.png')
    #
    # # 关闭
    # def test_class_exit_close(self):
    #     self.test_class_video_close()
    #     button_close = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_close")
    #     button_close.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/exit/close.png')
    #
    # # 退出运动
    # def test_class_exit_quit(self):
    #     self.test_class_video_close()
    #     button_quit = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnQuit")
    #     button_quit.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/exit/quit.png')
    #
    # # 休息一会儿
    # def test_class_exit_snooze(self):
    #     self.test_class_video_close()
    #     button_snooze = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnSnooze")
    #     button_snooze.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/exit/snooze.png')

    # # 运动完成页
    # def test_class_done(self):
    #     self.swipeUpToCla()
    #     enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     enter_classic.click()
    #     sleep(2)
    #     button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     button_go.click()
    #     sleep(2)
    #     button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
    #     button_go2.click()
    #     sleep(2)
    #     count = 0
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/done/' + str(count) + '.png')
    #     while count < 13:
    #         button_next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_next")
    #         button_next.click()
    #         sleep(2)
    #         count = count + 1
    #         self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/done/' + str(count) + '.png')
    #     sleep(40)
    #
    # # 运动完成页-添加/修改体重
    # def test_class_done_weight(self):
    #     self.test_class_done()
    #     try:
    #         button_cancel = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_cancel")
    #         button_cancel.click()
    #     except:
    #         pass
    #     current_weight = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/current_weight_tv")
    #     current_weight.click()
    #     edit_weight = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/edit_weight")
    #     edit_weight.clear()
    #     edit_weight.send_keys("70")
    #     edit_height = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/edit_height")
    #     edit_height.clear()
    #     edit_height.send_keys("180")
    #     button_save = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnSave")
    #     button_save.click()
    #     sleep(2)
    #     self.sh('adb shell input keyevent 4')
    #     sleep(1)
    #     self.sh('adb shell input keyevent 4')
    #     self.switch_tap(1)
    #     currentWeight = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/currentWeight")
    #     currentHeight = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/currentHeight")
    #     self.assertIn('70', currentWeight.text)
    #     self.assertIn('180', currentHeight.text)
    #
    # # 运动完成页-再来一次
    # def test_class_done_again(self):
    #     self.test_class_done()
    #     try:
    #         button_cancel = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_cancel")
    #         button_cancel.click()
    #     except:
    #         pass
    #     again = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Once again")')
    #     again.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/done/again.png')
    #
    # # 运动完成页-分享
    # def test_class_done_share(self):
    #     pass
    #
    # # 分享页
    # def test_share(self):
    #     pass
    #
    # # 运动页
    # def test_workout(self):
    #     pass
    #
    # # 记录页
    # def test_track(self):
    #     pass
    #
    # # 成就页
    # def test_achievement(self):
    #     pass

    # # 初次打开app
    # def test_enter_choice_item(self):
    #     item_button = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/item_button")
    #     item_button[2].click()
    #     sleep(2)
    #     next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/next")
    #     next.click()
    #     sleep(2)
    #     start = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_ok")
    #     start.click()
    #
    # # 去除广告
    # def test_setting_ad(self):
    #     setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
    #     setting.click()
    #     remove_ad = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/"
    #                                                "setting_item_premium_entry")
    #     remove_ad.click()
    #     sleep(1)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/after_click_remove_ad.png')
    #     remove_ad_close = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/iv_close")
    #     remove_ad_close.click()
    #
    # # 添加提醒
    # def test_setting_reminder_add(self):
    #     setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
    #     setting.click()
    #     add_reminder = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/add_tag")
    #     add_reminder.click()
    #     reminder_label = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/reminder_program")
    #     reminder_label.click()
    #     label_list = self.driver.find_elements_by_class_name("android.widget.LinearLayout")
    #     label_list[2].click()
    #     repeat_day = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/day_check")
    #     repeat_day[0].click()
    #     save = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnRight")
    #     save.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/reminder_add.png')
    #
    # # 关闭提醒
    # def test_setting_reminder_off(self):
    #     setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
    #     setting.click()
    #     switch_reminder = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/switch_btn")
    #     switch_reminder[0].click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/reminder_off.png')
    #
    # # 打开提醒
    # def test_setting_reminder_on(self):
    #     setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
    #     setting.click()
    #     switch_reminder = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/switch_btn")
    #     switch_reminder[0].click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/reminder_on.png')
    #
    # # 删除提醒
    # def test_setting_reminder_delete(self):
    #     setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
    #     setting.click()
    #     reminder_list = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/program_info")
    #     reminder_list[0].click()
    #     sleep(2)
    #     self.swipeUp()
    #     button_delete = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/reminder_delete_btn")
    #     button_delete.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/delete_done.png')
    #
    # # 修改提醒
    # def test_setting_reminder_update(self):
    #     setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
    #     setting.click()
    #     reminder_list = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/program_info")
    #     reminder_list[0].click()
    #     reminder_label = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/reminder_program")
    #     reminder_label.click()
    #     label_list = self.driver.find_elements_by_class_name("android.widget.LinearLayout")
    #     label_list[1].click()
    #     reminder_time = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/reminder_time")
    #     reminder_time.click()
    #     sleep(1)
    #     button_ok = self.driver.find_element_by_id("android:id/button1")
    #     button_ok.click()
    #     self.swipeUp()
    #     repeat_day = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/day_check")
    #     repeat_day[3].click()
    #     repeat_day[4].click()
    #     repeat_day[5].click()
    #     repeat_day[6].click()
    #     save = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnRight")
    #     save.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/reminder_update.png')
    #
    # # 反馈意见
    # def test_setting_feedback(self):
    #     setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
    #     setting.click()
    #     self.swipeUp()
    #     sleep(2)
    #     feedback = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/feedback")
    #     feedback.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/feedback.png')
    #
    # # 分享应用
    # def test_setting_share(self):
    #     setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
    #     setting.click()
    #     self.swipeUp()
    #     sleep(2)
    #     share = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/share")
    #     share.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/share.png')
    #
    # # 隐私政策
    # def test_setting_privacy(self):
    #     setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
    #     setting.click()
    #     self.swipeUp()
    #     sleep(2)
    #     privacy = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/"
    #                                              "view_setting_item_privacy_policy")
    #     privacy.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/privacy.png')
    #
    # # 版本号
    # def test_setting_version(self):
    #     version = "1.6.1"
    #     setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
    #     setting.click()
    #     self.swipeUp()
    #     sleep(2)
    #     versionText = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/version")
    #     self.assertEqual(versionText.text, version)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/version.png')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AbsWorkoutTest)
    unittest.TextTestRunner(verbosity=2).run(suite)