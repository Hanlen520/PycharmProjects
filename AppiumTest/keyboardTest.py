import subprocess
import unittest
from time import sleep
from appium import webdriver

screenshot_path = '/Users/a140/Desktop/screenshotofkeyboard'

class keyboardTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['appPackage'] = 'com.emoji.keyboard.touchpal'
        desired_caps['appActivity'] = 'com.cootek.rnstore.StoreEntryActivity'
        desired_caps['noReset'] = True
        desired_caps['deviceName'] = 'HT6CA1700126'
        desired_caps['autoGrantPermissions'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_enter(self):
        # self.sh('adb shell am start -n com.emoji.keyboard.touchpal/com.cootek.rnstore.StoreEntryActivity')
        # print("helloword")
        # sleep(10)
        # self.driver.findElementByXPath("//android.view.ViewGroup[contains(@index,1)]").click()
        # sleep(10)
        # item_list = self.driver.find_elements_by_class_name("android.view.ViewGroup")
        # item_list[7].click()
        # self.swipeRight()
        # print("hello")
        # self.openC()
        # sleep(10)
        self.swipeLeft()
        sleep(10)

    # 获取屏幕宽度和高度
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    # def swipeRight(self):
    #     l = self.getSize()
    #     x1 = int(l[0])
    #     y1 = int(l[1] * 0.5)
    #     x2 = int(l[0] * 0.9)
    #     self.driver.swipe(x1, y1, x2, y1)

    # 向左滑动
    def swipeLeft(self):
        l = self.getSize()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(keyboardTest)
    unittest.TextTestRunner(verbosity=2).run(suite)