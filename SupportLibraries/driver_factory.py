""" This module contains the singleton driver instance implementation"""

import logging
import os
from appium import webdriver
from FrameworkUtilities.config_utility import ConfigUtility
from FrameworkUtilities.logger_utility import custom_logger


class DriverFactory:
    """
    This class contains the reusable methods for getting the driver instances
    """
    log = custom_logger(logging.INFO)
    config = ConfigUtility()

    def __init__(self, platform="android"):
        self.platform = platform
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.prop = self.config.load_properties_file()

    def get_driver_instance(self):

        if self.platform == "android":

            app_location = os.path.join(self.cur_path, r"../MobileApp/", self.prop.get('Cap_Android', 'app_name'))

            desired_caps = {
                'automationName': self.prop.get('Cap_Android', 'automation_name'),
                'deviceName': self.prop.get('Cap_Android', 'device_name'),
                'udid': self.prop.get('Cap_Android', 'ud_id'),
                'platformName': self.prop.get('App', 'platform'),
                'platformVersion': self.prop.get('Cap_Android', 'platform_version'),
                'appPackage': self.prop.get('Cap_Android', 'app_package'),
                'appActivity': self.prop.get('Cap_Android', 'app_activity'),
                #'app': app_location,
                'noReset': self.prop.get('Cap_Android', 'no_reset'),
                'autoGrantPermissions': self.prop.get('Cap_Android', 'auto_grant_permissions'),
                'unlockType':self.prop.get('Cap_Android', 'unlockType'),
                'unlockKey': self.prop.get('Cap_Android', 'unlockKey')

            }

            driver = webdriver.Remote(command_executor=self.prop.get('Grid', 'appium_server'),desired_capabilities=desired_caps)

            return driver

        elif self.platform == "ios":
            pass

        elif self.platform == "browserstack_mobile":

            username = self.prop.get('BrowserStack', 'bs_username')
            automate_key = self.prop.get('BrowserStack', 'bs_key')
            url = "http://{}:{}@hub.browserstack.com:80/wd/hub".format(username, automate_key)

            caps = {
                    'name': self.prop.get('Cap_Cloud', 'cloud_name'),
                    'device': self.prop.get('Cap_Cloud', 'cloud_device_name'),
                    'platformVersion': self.prop.get('Cap_Cloud', 'cloud_platform_version'),
                    'app': self.prop.get('BrowserStack', 'bs_app_hash'),
                    'appPackage': self.prop.get('Cap_Cloud', 'cloud_app_package'),
                    'appActivity': self.prop.get('Cap_Cloud', 'cloud_app_activity'),
                    'noReset': self.prop.get('Cap_Cloud', 'cloud_no_reset'),
                    'autoGrantPermissions': self.prop.get('Cap_Cloud', 'cloud_auto_grant_permissions')

                    }

            driver = webdriver.Remote(command_executor=url,desired_capabilities=caps)
            return driver

        elif self.platform == "SauceLabs":

            username = self.prop.get('SauceLabs', 'sl_username')
            automate_key = self.prop.get('SauceLabs', 'sl_key')
            url = "https://{}:{}@ondemand.saucelabs.com:443/wd/hub".format(username, automate_key)

            caps = {'name': self.prop.get('Cap_Cloud', 'cloud_name'),
                    'device': self.prop.get('Cap_Cloud', 'cloud_device_name'),
                    'platformVersion': self.prop.get('Cap_Cloud', 'cloud_platform_version'),
                    'app': self.prop.get('SauceLabs', 'sl_app_hash'),
                    'appPackage': self.prop.get('Cap_Cloud', 'cloud_app_package'),
                    'appActivity': self.prop.get('Cap_Cloud', 'cloud_app_activity'),
                    'noReset': self.prop.get('Cap_Cloud', 'cloud_no_reset'),
                    'autoGrantPermissions': self.prop.get('Cap_Cloud', 'cloud_auto_grant_permissions')}

            driver = webdriver.Remote(command_executor=url,desired_capabilities=caps)
