import unittest
from appium import webdriver

class HelloWorld(unittest.TestCase):
    def test_enterFilter(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['app'] = '/Users/a140/Downloads/filter-点传-0518.apk'
        desired_caps['deviceName'] = '03083025d0250909'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)
        #向左滑动跳过引导页
        x = 0
        while x < 3:
            self.swipeLeft()
            x += 1
        enterApp = self.driver.find_element_by_id("com.eyefilter.night:id/enter")
        enterApp.click()

    #获取屏幕宽度和高度
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    #向左滑动
    def swipeLeft(self):
        l = self.getSize()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HelloWorld)
    unittest.TextTestRunner(verbosity=2).run(suite)