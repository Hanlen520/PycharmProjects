import unittest
from appium import webdriver
from time import sleep


class HelloWorld(unittest.TestCase):
    def test_addContact(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['appPackage'] = 'com.android.contacts'
        desired_caps['appActivity'] = 'com.android.contacts.activities.PeopleActivity'
        desired_caps['deviceName'] = 'N8K7N17606003031'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        #新建联系人
        createContactButton = self.driver.find_element_by_id("com.android.contacts:id/menu_add_contact")
        createContactButton.click()
        sleep(5)
        self.driver.save_screenshot("afterclick.png")
        # #添加姓名
        # name = self.driver.find_element_by_name(u"姓名")
        # name.click()
        # name.send_keys("appiumTest")
        # #添加号码
        # telephoneControls = self.driver.find_elements_by_name(u"电话号码")
        # telephoneControls[0].click()
        # telephoneControls[0].send_keys("01012345678")
        # #截图
        # self.driver.save_screenshot("afterinput.png")
        # #点击完成按钮
        # completement = self.driver.find_element_by_id("android:id/icon2")
        # completement.click()
        # #对照姓名
        # contactName = self.driver.find_element_by_id("com.android.contacts:id/name")
        # self.assertEqual(contactName.text, "appiumTest")
        # #对照号码
        # contactData = self.driver.find_element_by_id("com.android.contacts:id/data")
        # self.assertEqual(contactData[0].text, "01012345678")
        # #截图
        # self.driver.save_screenshot("newContact.png")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(HelloWorld)
    unittest.TextTestRunner(verbosity=2).run(suite)