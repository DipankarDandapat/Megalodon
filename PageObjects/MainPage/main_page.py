"""This module is used for main page objects."""

import logging

from selenium.webdriver import ActionChains

from SupportLibraries.base_helpers import BaseHelpers
from FrameworkUtilities import logger_utility as log_utils
# import FrameworkUtilities.logger_utility as log_utils
import time
from appium.webdriver.common.touch_action import TouchAction


class MainPage(BaseHelpers):
    """This class defines the method and element identifications for main page."""

    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.loginPage_locators = self.pageLocators('HomePage')

    # team_A_super_tackle = "//android.widget.Button[@resource-id='com.example.android.prokabaddi:id/button_STackle']"
    # team_B_super_tackle = "//android.widget.Button[@resource-id='com.example.android.prokabaddi:id/button_STackle_b']"
    # team_A_do_or_die_raid = "//android.widget.Button[@resource-id='com.example.android.prokabaddi:id/button_DRaid']"
    # team_B_do_or_die_raid = "//android.widget.Button[@resource-id='com.example.android.prokabaddi:id/button_DRaid']"
    # team_A_touch = "//android.widget.Button[@resource-id='com.example.android.prokabaddi:id/button_Touch']"
    # team_B_touch = "//android.widget.Button[@resource-id='com.example.android.prokabaddi:id/button_Touch_b']"


    # def verify_main_screen_mobile(self):
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'android_view_mobile'))
    #     time.sleep(10)
    #     self.sendKeys("9800188406",*self.locator(self.loginPage_locators, 'mobile_number_box'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'mobile_number_process'))
    #     time.sleep(5)
    #     self.sendKeys("Welcome@2020", *self.locator(self.loginPage_locators, 'password_box'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'view_password_button'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'LoginButton'))
    #     time.sleep(10)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'ProfileButton'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'KYCButton'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'Selfie'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'SelfieStartbutton'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'captureBtn'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'captureBtnsave'))
    #     time.sleep(10)
    #     self.clearKeys(*self.locator(self.loginPage_locators, 'pancard'))
    #     time.sleep(5)
    #     self.sendKeys("BTQPD0105Z", *self.locator(self.loginPage_locators, 'pancard'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'KycType'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'selectPassport'))
    #     time.sleep(5)
    #     self.clearKeys(*self.locator(self.loginPage_locators, 'KycDocNum'))
    #     time.sleep(5)
    #     self.sendKeys("BTQPD0105Z", *self.locator(self.loginPage_locators, 'KycDocNum'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'imgFront'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'OPENPHOTOS'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'selectphoto'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'saveimage'))
    #     time.sleep(7)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'imgBack'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'OPENPHOTOS'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'selectphoto'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'saveimage'))
    #     time.sleep(7)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'SUBMIT'))
    #     time.sleep(10)


    # def verify_Basic_Information(self):
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'android_view_mobile'))
    #     time.sleep(10)
    #     self.sendKeys("9800188406",*self.locator(self.loginPage_locators, 'mobile_number_box'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'mobile_number_process'))
    #     time.sleep(5)
    #     self.sendKeys("Welcome@2020", *self.locator(self.loginPage_locators, 'password_box'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'LoginButton'))
    #     time.sleep(10)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'ProfileButton'))
    #     time.sleep(5)
    #     self.elementClick(*self.locator(self.loginPage_locators, 'BasicInformation'))

        # self.clearKeys(*self.locator(self.loginPage_locators, 'FirstName'))
        # time.sleep(5)
        # self.sendKeys("dipankar", *self.locator(self.loginPage_locators, 'FirstName'))
        # time.sleep(5)
        #
        # self.clearKeys(*self.locator(self.loginPage_locators, 'MiddleName'))
        # time.sleep(5)
        # self.sendKeys("d", *self.locator(self.loginPage_locators, 'MiddleName'))
        # time.sleep(5)
        # self.clearKeys(*self.locator(self.loginPage_locators, 'LastName'))
        # time.sleep(5)
        # self.sendKeys("dandapat", *self.locator(self.loginPage_locators, 'LastName'))
        # time.sleep(5)
        #
        # time.sleep(5)
        # self.elementClick(*self.locator(self.loginPage_locators, 'gender'))
        # time.sleep(5)
        # self.elementClick(*self.locator(self.loginPage_locators, 'dob'))
        # time.sleep(10)
        # self.elementClick(*self.locator(self.loginPage_locators, 'year'))
        # time.sleep(10)
        # year_list = self.getElementList(*self.locator(self.loginPage_locators, 'yearlist'))
        # #year_list =self.driver.find_elements_by_xpath("//android.widget.TextView[@resource-id='android:id/text1']")
        # count = len(year_list)
        # self.log.info(count)
        #
        # for i in range(count):
        #     if year_list[i].text=="1982":
        #         self.log.info("1982 is presents")
        #         year_list[i].click()
        #         time.sleep(5)
        #         break
        #     else:
        #         TouchAction(self.driver).press(x=810, y=780).move_to(x=796, y=1579).release().perform()
        #
        # day_list=self.getElementList(*self.locator(self.loginPage_locators, 'daylist'))
        # count = len(day_list)
        # self.log.info(count)
        # for i in range(count):
        #     if day_list[i].text == "10":
        #         day_list[i].click()
        #         self.log.info("click on 10")
        #         time.sleep(5)
        #         break
        #
        # time.sleep(5)
        # self.elementClick(*self.locator(self.loginPage_locators, 'OKbutton'))
        #
        # time.sleep(5)
        # self.elementClick(*self.locator(self.loginPage_locators, 'maritalstatus'))
        # time.sleep(5)
        # self.elementClick(*self.locator(self.loginPage_locators, 'HighestQualification'))
        # time.sleep(5)
        # list_of_Qualification=self.getElementList(*self.locator(self.loginPage_locators, 'Qualificationtitle'))
        # count = len(list_of_Qualification)
        # for i in range(count):
        #     if list_of_Qualification[i].text == "Professional":
        #         list_of_Qualification[i].click()
        #         self.log.info("Professional click")
        #         time.sleep(5)
        #         break
        #
        # self.clearKeys(*self.locator(self.loginPage_locators, 'FatherName'))
        # time.sleep(5)
        # self.sendKeys("deeep d", *self.locator(self.loginPage_locators, 'FatherName'))
        # time.sleep(5)
        # self.clearKeys(*self.locator(self.loginPage_locators, 'MotherName'))
        # time.sleep(5)
        # self.sendKeys("deeep dmmmmmmm", *self.locator(self.loginPage_locators, 'MotherName'))
        # time.sleep(5)
        # self.elementClick(*self.locator(self.loginPage_locators, 'NextButton'))
        # time.sleep(5)
        # self.sendKeys("Bangalore", *self.locator(self.loginPage_locators, 'PermanentAddress'))
        # time.sleep(5)
        # self.clearKeys(*self.locator(self.loginPage_locators, 'PermanentPinCode'))
        # self.elementClick(*self.locator(self.loginPage_locators, 'PermanentPinCode'))
        # self.sendKeys("56003", *self.locator(self.loginPage_locators, 'PermanentPinCode'))
        # time.sleep(6)
        # TouchAction(self.driver).press(x=210, y=1020).release().perform()
        # time.sleep(5)
        # addresscheckbox=self.isElementChecked(*self.locator(self.loginPage_locators, 'CurrentAddressCheckBox'))
        # self.log.info(addresscheckbox)
        # if addresscheckbox=="true":
        #     self.log.info("@@@@@@@@@@@@@@@@@@@@@address checkbox already checked")
        # else:
        #     self.elementClick(*self.locator(self.loginPage_locators, 'CurrentAddressCheckBox'))
        #
        # time.sleep(5)
        # self.nev_back()
        # time.sleep(6)
        # self.elementClick(*self.locator(self.loginPage_locators, 'NextButton'))
        # time.sleep(6)
        # self.elementClick(*self.locator(self.loginPage_locators, 'btnNo'))
        # time.sleep(6)
        # self.elementClick(*self.locator(self.loginPage_locators, 'MobileNumber'))
        # self.sendKeys("9999999999", *self.locator(self.loginPage_locators, 'MobileNumber'))
        # time.sleep(10)
        # Nextbutton=self.isElementDisplayed(*self.locator(self.loginPage_locators, 'NextButton'))
        # if Nextbutton==True:
        #     self.elementClick(*self.locator(self.loginPage_locators, 'NextButton'))
        # else:
        #     time.sleep(5)
        #     self.nev_back()
        #     time.sleep(5)
        #     self.elementClick(*self.locator(self.loginPage_locators, 'NextButton'))
        #
        #
        # time.sleep(6)

    def verify_Employment_Information(self):
        time.sleep(5)
        # self.elementClick(*self.locator(self.loginPage_locators, 'android_view_mobile'))
        # time.sleep(10)
        # self.sendKeys("9800188406", *self.locator(self.loginPage_locators, 'mobile_number_box'))
        # time.sleep(5)
        # self.elementClick(*self.locator(self.loginPage_locators, 'mobile_number_process'))
        # time.sleep(5)
        # self.sendKeys("Welcome@2020", *self.locator(self.loginPage_locators, 'password_box'))
        # time.sleep(5)
        # self.elementClick(*self.locator(self.loginPage_locators, 'LoginButton'))
        time.sleep(10)
        self.elementClick(*self.locator(self.loginPage_locators, 'ProfileButton'))
        time.sleep(5)
        self.elementClick(*self.locator(self.loginPage_locators, 'EmploymentInformation'))
        time.sleep(5)
        self.elementClick(*self.locator(self.loginPage_locators, 'CompanyName'))
        time.sleep(5)
        self.sendKeys("TATA SKY", *self.locator(self.loginPage_locators, 'CompanyName'))
        time.sleep(5)
        self.clearKeys(*self.locator(self.loginPage_locators, 'CompanyName'))
        time.sleep(5)
        self.sendKeys("TATA SKY ", *self.locator(self.loginPage_locators, 'CompanyName'))
        time.sleep(5)
        TouchAction(self.driver).press(x=227, y=568).release().perform()
        time.sleep(5)
        self.elementClick(*self.locator(self.loginPage_locators, 'OfficeAddress'))
        time.sleep(5)
        self.sendKeys("8/1,Bangalore", *self.locator(self.loginPage_locators, 'OfficeAddress'))
        time.sleep(5)
        self.elementClick(*self.locator(self.loginPage_locators, 'OfficePincode'))
        self.sendKeys("560032", *self.locator(self.loginPage_locators, 'OfficePincode'))
        time.sleep(6)
        TouchAction(self.driver).press(x=320, y=1102).release().perform()
        time.sleep(5)
        self.elementClick(*self.locator(self.loginPage_locators, 'NextButton'))
        time.sleep(5)
        self.sendKeys("12000", *self.locator(self.loginPage_locators, 'HomeSalary'))
        time.sleep(5)
        self.sendKeys("12000", *self.locator(self.loginPage_locators, 'Designation'))
        time.sleep(5)
        self.elementClick(*self.locator(self.loginPage_locators, 'JoiningDate'))
        time.sleep(5)
        self.elementClick(*self.locator(self.loginPage_locators, 'JoiningDate_year'))
        time.sleep(5)
        year_list = self.getElementList(*self.locator(self.loginPage_locators, 'JoiningDate_year_list'))
        count = len(year_list)
        self.log.info(count)
        for i in range(count):
            if year_list[i].text=="2017":
                self.log.info("2017 is presents")
                year_list[i].click()
                time.sleep(5)
                break

        day_list = self.getElementList(*self.locator(self.loginPage_locators, 'JoiningDatedaylist'))
        count = len(day_list)
        self.log.info(count)
        for i in range(count):
            if day_list[i].text == "10":
                day_list[i].click()
                self.log.info("click on 10")
                time.sleep(5)
                break

        time.sleep(5)
        self.elementClick(*self.locator(self.loginPage_locators, 'OKbutton'))
        time.sleep(5)
        self.elementClick(*self.locator(self.loginPage_locators, 'EmploymentProof'))
        time.sleep(5)
        list_of_Qualification=self.getElementList(*self.locator(self.loginPage_locators, 'EmploymentProofList'))
        count = len(list_of_Qualification)
        for i in range(count):
            if list_of_Qualification[i].text == "Joining letter":
                list_of_Qualification[i].click()
                self.log.info("Joining letter")
                time.sleep(5)
                break

        time.sleep(5)
        self.elementClick(*self.locator(self.loginPage_locators, 'UploadEmploymentProof'))
        time.sleep(5)
        self.elementClick(*self.locator(self.loginPage_locators, 'UploadPhotosFromGallery'))
        time.sleep(10)









    # def verify_main_screen_elements(self):
    #     """
    #     This function is used to verify all the elements present on the main screen
    #     :return: this function returns boolean status of element located
    #     """
    #     result = False
    #     _xpath_prop = "xpath"
    #
    #     locator_dict = {
    #         self.team_A_super_tackle: _xpath_prop,
    #         self.team_B_super_tackle: _xpath_prop,
    #         self.team_A_do_or_die_raid: _xpath_prop,
    #         self.team_B_do_or_die_raid: _xpath_prop,
    #         self.team_A_touch: _xpath_prop,
    #         self.team_B_touch: _xpath_prop,
    #         self.team_A_all_out: _xpath_prop,
    #         self.team_B_all_out: _xpath_prop,
    #         self.team_A_bonus: _xpath_prop,
    #         self.team_B_bonus: _xpath_prop,
    #         self.team_A_tackle: _xpath_prop,
    #         self.team_B_tackle: _xpath_prop,
    #         self.reset_button: _xpath_prop,
    #         self.team_A_score_view: _xpath_prop,
    #         self.team_B_score_view: _xpath_prop
    #     }
    #
    #     result = self.verify_elements_located(locator_dict)
    #
    #     if not result:
    #         self.log.error("Main screen element verification failed.")
    #
    #     return result
    #
    # def verify_super_tackle_functionality(self, move_point):
    #     """
    #     This function is used to verify super tackle functionality.
    #     :return: this function returns boolean status for super tackle functionality.
    #     """
    #     result = True
    #
    #     self.mouse_click_action(self.team_A_super_tackle)
    #     self.wait_for_sync(1)
    #     actual_point = self.get_text_from_element(self.team_A_score_view)
    #
    #     if not self.verify_text_match(actual_point, str(move_point)):
    #         self.log.error("Super tackle move point is not correct.")
    #         result = False
    #
    #     return result
    #
    # def verify_reset_button_functionality(self):
    #     """
    #     This function is used to verify reset functionality.
    #     :return: this function returns boolean status for reset functionality.
    #     """
    #     result = True
    #
    #     self.mouse_click_action(self.reset_button)
    #     self.wait_for_sync(1)
    #     actual_score_value = self.get_text_from_element(self.team_A_score_view)
    #
    #     if not self.verify_text_match(actual_score_value, "0"):
    #         self.log.error("Reset button functionality is not working.")
    #         result = False
    #
    #     return result
