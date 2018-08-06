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

    # 初次打开app
    def test_enter_choice_item(self):
        item_button = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/item_button")
        item_button[2].click()
        sleep(2)
        next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/next")
        next.click()
        sleep(2)
        start = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_ok")
        start.click()

    # 去除广告
    def test_setting_ad(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        remove_ad = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/"
                                                   "setting_item_premium_entry")
        remove_ad.click()
        sleep(1)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/after_click_remove_ad.png')
        remove_ad_close = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/iv_close")
        remove_ad_close.click()

    # 添加提醒
    def test_setting_reminder_add(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        add_reminder = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/add_tag")
        add_reminder.click()
        reminder_label = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/reminder_program")
        reminder_label.click()
        label_list = self.driver.find_elements_by_class_name("android.widget.LinearLayout")
        label_list[2].click()
        repeat_day = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/day_check")
        repeat_day[0].click()
        save = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnRight")
        save.click()
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/reminder_add.png')

    # 关闭提醒
    def test_setting_reminder_off(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        switch_reminder = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/switch_btn")
        switch_reminder[0].click()
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/reminder_off.png')

    # 打开提醒
    def test_setting_reminder_on(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        switch_reminder = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/switch_btn")
        switch_reminder[0].click()
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/reminder_on.png')

    # 删除提醒
    def test_setting_reminder_delete(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        reminder_list = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/program_info")
        reminder_list[0].click()
        sleep(2)
        self.swipeUp()
        button_delete = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/reminder_delete_btn")
        button_delete.click()
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/delete_done.png')

    # 修改提醒
    def test_setting_reminder_update(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        reminder_list = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/program_info")
        reminder_list[0].click()
        reminder_label = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/reminder_program")
        reminder_label.click()
        label_list = self.driver.find_elements_by_class_name("android.widget.LinearLayout")
        label_list[1].click()
        reminder_time = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/reminder_time")
        reminder_time.click()
        sleep(1)
        button_ok = self.driver.find_element_by_id("android:id/button1")
        button_ok.click()
        self.swipeUp()
        repeat_day = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/day_check")
        repeat_day[3].click()
        repeat_day[4].click()
        repeat_day[5].click()
        repeat_day[6].click()
        save = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnRight")
        save.click()
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/reminder_update.png')

    # 反馈意见
    def test_setting_feedback(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        self.swipeUp()
        sleep(2)
        feedback = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/feedback")
        feedback.click()
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/feedback.png')

    # 分享应用
    def test_setting_share(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        self.swipeUp()
        sleep(2)
        share = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/share")
        share.click()
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/share.png')

    # 隐私政策
    def test_setting_privacy(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        self.swipeUp()
        sleep(2)
        privacy = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/"
                                                 "view_setting_item_privacy_policy")
        privacy.click()
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/privacy.png')

    # 版本号
    def test_setting_version(self):
        version = "1.6.1"
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        self.swipeUp()
        sleep(2)
        versionText = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/version")
        self.assertEqual(versionText.text, version)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/version.png')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AbsWorkoutTest)
    unittest.TextTestRunner(verbosity=2).run(suite)