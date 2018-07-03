import subprocess
import unittest
from time import sleep
from appium import webdriver

screenshot_path = '/Users/a140/Desktop/ScreenShotOfFilter/'


class FilterTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['app'] = '/Users/a140/Downloads/filter-点传-0518.apk'
        desired_caps['appWaitActivity'] = 'com.eyefilter.night.activity.GuideActivity'
        desired_caps['deviceName'] = '03083025d0250909'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)

    def tearDown(self):
        self.driver.quit()

    def enter(self):
        # 向左滑动跳过引导页
        x = 0
        while x < 3:
            self.swipeLeft()
            x += 1
        enter_app = self.driver.find_element_by_id("com.eyefilter.night:id/enter")
        enter_app.click()
        sleep(3)

    # 获取屏幕宽度和高度
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    # 向左滑动
    def swipeLeft(self):
        l = self.getSize()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1)

    # 开启关闭护目镜/调整护目镜颜色
    def test_filter(self):
        self.enter()
        print("开启关闭护目镜/调整护目镜颜色case")
        filter_switch = self.driver.find_element_by_id("com.eyefilter.night:id/mSwitch")
        print("开启护目镜")
        filter_switch.click()
        sleep(3)
        self.driver.get_screenshot_as_file(screenshot_path + "filter_on.png")
        try:
            print("关闭护目镜")
            filter_switch.click()
            print("开启Auto Enable")
            enable = self.driver.find_element_by_id("android:id/button1")
            enable.click()
            sleep(4)
            self.driver.get_screenshot_as_file(screenshot_path + "auto_enable_on.png")
        except:
            pass
        self.driver.implicitly_wait(10)
        color1 = self.driver.find_element_by_id("com.eyefilter.night:id/change_color1")
        color1.click()
        sleep(2)
        self.driver.get_screenshot_as_file(screenshot_path + "filter_color1.png")
        self.driver.implicitly_wait(10)
        color2 = self.driver.find_element_by_id("com.eyefilter.night:id/change_color2")
        color2.click()
        sleep(2)
        self.driver.get_screenshot_as_file(screenshot_path + "filter_color2.png")
        self.driver.implicitly_wait(10)
        color3 = self.driver.find_element_by_id("com.eyefilter.night:id/change_color3")
        color3.click()
        sleep(2)
        self.driver.get_screenshot_as_file(screenshot_path + "filter_color3.png")
        self.driver.implicitly_wait(10)
        color4 = self.driver.find_element_by_id("com.eyefilter.night:id/change_color4")
        color4.click()
        sleep(2)
        self.driver.get_screenshot_as_file(screenshot_path + "filter_color4.png")
        color5 = self.driver.find_element_by_id("com.eyefilter.night:id/change_color5")
        color5.click()
        sleep(3)
        self.driver.get_screenshot_as_file(screenshot_path + "filter_color5.png")
        self.sh('adb shell input keyevent 4')

    # 返回键(back)
    def sh(self, command):
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(p.stdout.read())

    # 调整护目镜透明度
    def test_swipe_alpha(self):
        self.enter()
        print("调整护目镜透明度case")
        self.driver.get_screenshot_as_file(screenshot_path + "before_swipe_alpha.png")
        self.driver.implicitly_wait(10)
        swipe_view = self.driver.find_element_by_id("com.eyefilter.night:id/seek_bar")
        x = swipe_view.location.get('x')
        y = swipe_view.location.get('y')
        width = swipe_view.size.get('width')
        height = swipe_view.size.get('height')
        print(x, y, width, height)
        # offset = width / 6
        p1 = int(x + width / 6), int(y + height / 2)
        p2 = int(x + width / 2 + 125), int(y + height / 2)
        self.driver.swipe(p1[0], p1[1], p2[0], p2[1], 1000)
        sleep(3)
        self.driver.get_screenshot_as_file(screenshot_path + "after_swipe_alpha.png")

    # 护颈运动
    def test_neck_exercise(self):
        self.enter()
        print("护颈运动case")
        self.driver.implicitly_wait(10)
        menus = self.driver.find_elements_by_id("com.eyefilter.night:id/custom_text")
        menus[2].click()
        self.driver.implicitly_wait(10)
        startexer = self.driver.find_element_by_id("com.eyefilter.night:id/preference_neck_exercise")
        startexer.click()
        sleep(2)
        self.driver.get_screenshot_as_file(screenshot_path + "start_exer.png")
        sleep(10)
        self.driver.get_screenshot_as_file(screenshot_path + "between_exer.png")
        sleep(10)
        self.driver.get_screenshot_as_file(screenshot_path + "after_exer.png")
        self.sh('adb shell input keyevent 4')

    # 通知栏显示
    def test_isnotiopen(self):
        self.enter()
        print("通知栏显示case")
        self.driver.implicitly_wait(10)
        menus = self.driver.find_elements_by_id("com.eyefilter.night:id/custom_text")
        menus[2].click()
        sleep(3)
        # 上滑手势，屏幕移动到下半部分
        self.sh('adb shell input swipe 300 1000 300 500')
        self.driver.implicitly_wait(10)
        noti = self.driver.find_element_by_id("com.eyefilter.night:id/preference_notification")
        self.driver.open_notifications()
        sleep(3)
        self.driver.get_screenshot_as_file(screenshot_path + "before_clicknoti.png")
        self.driver.keyevent(4)
        sleep(3)
        noti.click()
        sleep(3)
        self.driver.open_notifications()
        sleep(3)
        self.driver.get_screenshot_as_file(screenshot_path + "after_clicknoti.png")
        self.driver.keyevent(4)
        sleep(3)
        noti.click()

    # 反馈
    def test_feedback(self):
        self.enter()
        print("反馈case")
        self.driver.implicitly_wait(10)
        menus = self.driver.find_elements_by_id("com.eyefilter.night:id/custom_text")
        menus[2].click()
        sleep(3)
        # 上滑手势，屏幕移动到下半部分
        self.sh('adb shell input swipe 300 1000 300 500')
        self.driver.implicitly_wait(30)
        feed = self.driver.find_element_by_id("com.eyefilter.night:id/preference_feedback")
        feed.click()
        sleep(3)
        self.driver.keyevent(4)
        sleep(3)
        self.driver.get_screenshot_as_file(screenshot_path + "feedback.png")
        self.driver.keyevent(4)

    # 疲劳提醒
    def test_isfatiguropen(self):
        self.enter()
        print("疲劳提醒case")
        self.driver.implicitly_wait(10)
        menus = self.driver.find_elements_by_id("com.eyefilter.night:id/custom_text")
        menus[2].click()
        sleep(3)
        # 上滑手势，屏幕移动到下半部分
        self.sh('adb shell input swipe 300 1000 300 500')
        self.driver.implicitly_wait(10)
        fatigur = self.driver.find_element_by_id("com.eyefilter.night:id/preference_fatigue")
        fatigur.click()
        sleep(3)
        self.driver.get_screenshot_as_file(screenshot_path + "fatigur.png")

    # 通知栏开关
    def test_notiswitch(self):
        self.enter()
        print("通知栏开关case")
        self.driver.open_notifications()
        self.driver.implicitly_wait(10)
        switchnoti = self.driver.find_element_by_id("com.eyefilter.night:id/toggle_filter")
        switchnoti.click()
        sleep(10)
        self.driver.keyevent(4)
        sleep(10)
        self.driver.keyevent(4)
        sleep(3)
        self.driver.get_screenshot_as_file(screenshot_path + "afternoticlose.png")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FilterTest)
    unittest.TextTestRunner(verbosity=2).run(suite)