import unittest
from appium import webdriver
import logging
import FrameworkUtilities.logger_utility as log_utils
""" 
There are the following limitations:

Real Devices
Changing Airplane Mode state only works for Android 6 and older
Chaning data connection state works for Android 4.4 and older. Newer OS releases (5.0+) must be rooted in order to make the feature working
Changing Wi-Fi connection state should work for all Android versions

Emulators
Changing Airplane Mode state only works for Android 6 and older
Chaning data connection state should work for all Android versions
Changing Wi-Fi connection state should work for all Android versions
"""
import time
class NetworkConnectionTests(unittest.TestCase):
    log = log_utils.custom_logger(logging.INFO)
    def setUp(self):
        capabilities={'platformName': 'Android','deviceName': 'Redmi Note 9','platformVersion': '10','automationName': 'UIAutomator2','autoLaunch':'false',
                      'ud_id':'1a277e550403','unlockType':'pattern','unlockKey':'12369',
                      'app':'D:/Python_Projects/AppiumPythonHybridFramework-master/MobileApp/demo.apk'
                      }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)

    def tearDown(self):
        self.driver.quit()

    # def test_lock(self):
    #     time.sleep(10)
    #     self.driver.lock(-1)
    #     time.sleep(10)
    #     self.driver.unlock()
    #     time.sleep(10)
        # try:
        #     self.assertTrue(self.driver.is_locked())
        # finally:
        #     self.driver.unlock()
        # self.assertFalse(self.driver.is_locked())

    # def test_close__and_launch_app(self):
    #     el = self.driver.find_element_by_name('Weather')
    #     self.assertIsNotNone(el)
    #
    #     self.driver.close_app()
    #     self.driver.launch_app()
    #
    #     el = self.driver.find_element_by_name('Weather')
    #     self.assertIsNotNone(el)

    # def test_app_management(self):
    #     app_id = self.driver.current_package
    #     self.log.info(app_id)
    #
    #     self.log.info(self.driver.query_app_state(app_id))
    #     self.driver.background_app(-1)
    #     self.log.info(self.driver.query_app_state(app_id))
    #     #self.assertTrue(self.driver.query_app_state(app_id) <4)
    #     self.driver.activate_app(app_id)
    #     self.assertEqual(self.driver.query_app_state(app_id),4)

    def test_current_activity(self):
        self.driver.launch_app()
        time.sleep(10)
        activity = self.driver.current_activity
        self.log.info(activity)
        package = self.driver.current_package
        self.log.info(package)
        #self.driver.start_activity(package, activity)

        time.sleep(10)

        # self.log.info(package)
        # self.log.info(self.driver.background_app(1))
        # self.log.info(self.driver.is_app_installed('com.example.android.prokabaddi'))
        # self.driver.install_app('D:\\Python_Projects\\AppiumPythonHybridFramework-master\\MobileApp\\mpokket.apk')
        # self.driver.remove_app('com.example.android.prokabaddi')
        # self.log.info(self.driver.is_app_installed('com.example.android.prokabaddi'))
        # self.driver.open_notifications()
        # time.sleep(10)
        # x = self.driver.get_window_size()['width']
        # y = self.driver.get_window_size()['height']
        # self.log.info(x)
        # self.log.info(self.driver.background_app(5) )
        # self.driver.launch_app()
        # time.sleep(10)





if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(NetworkConnectionTests)
    unittest.TextTestRunner(verbosity=2).run(suite)