import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='ASUS_Z01RD',
    appPackage='com.mpokket.app.debug',
    appActivity='com.mpokket.app.loginandregistration.presentation.ui.activities.SplashActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        el = self.driver.find_element(by=MobileBy.XPATH, value='//*[@text="Battery"]')
        el.click()

if __name__ == '__main__':
    unittest.main()