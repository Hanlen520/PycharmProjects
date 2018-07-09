from appium import webdriver
import time
import unittest

screenshot_path = '/Users/a140/Desktop/ScreenShotOfNetease/'


class AppTask(unittest.TestCase):

    def basic(app_path):
        global driver
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.1'
        desired_caps['deviceName'] = '03083025d0250909'
        desired_caps['app'] = app_path
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(10)

    def tearDown(self):
        driver.quit()

    def test_001_wyy_music(self):
        AppTask.basic('/Users/a140/Downloads/CloudMusic_official_5.3.1.588831.apk')
        driver.find_element_by_id('com.netease.cloudmusic:id/kh').click()
        time.sleep(3)
        driver.find_element_by_id('com.netease.cloudmusic:id/abi').click()
        time.sleep(3)
        driver.find_element_by_id('com.netease.cloudmusic:id/gz').send_keys('email_address')
        time.sleep(3)
        driver.find_element_by_id('com.netease.cloudmusic:id/h0').send_keys('password')
        time.sleep(3)
        driver.find_element_by_id('com.netease.cloudmusic:id/h1').click()
        time.sleep(5)
        driver.find_element_by_id('com.netease.cloudmusic:id/ne').click()
        check_in = driver.page_source.find('已签到')
        if check_in != -1:
            print('今日已签到，明日再来')
            driver.save_screenshot('wyy.png')
        else:
            driver.find_element_by_id('com.netease.cloudmusic:id/a7d').click()
            time.sleep(5)
            driver.keyevent(4)
            time.sleep(1)
            driver.find_element_by_id('com.netease.cloudmusic:id/ne').click()
            driver.save_screenshot('done.png')

        self.assertIn('已签到', driver.page_source, msg='任务失败，请查看截图' + str(screenshot_path))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppTask)
    unittest.TextTestRunner(verbosity=2).run(suite)
