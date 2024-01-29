"""
This module contains most of the reusable functions to support test cases.
"""

import os
import time
import logging
from builtins import staticmethod
from traceback import print_stack
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import FrameworkUtilities.logger_utility as log_utils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


def readJson(jsonFilePath):
    with open(jsonFilePath) as f:
        jsonFile = json.load(f)

    return jsonFile


class UIHelpers():

    """
    UI Helpers class to contains all ui helper methods.
    """

    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver


    def pageLocators(self, page):
        """
        read the Locators of specific page
        :param page: page
        :return: list of all Locators in specific page
        """
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.locatorsPath = os.path.join(self.cur_path, r"../Locators/locators.json")
        locatorsJsonFile = readJson(self.locatorsPath)
        pageLocators = [locator for locator in locatorsJsonFile if locator['pageName'] in page]
        return pageLocators

    def locator(self, pageLocators, locatorName):
        """
        get specific locator in specific page
        :param pageLocators: specific page
        :param locatorName: locator name
        :return: locator and locator Type
        """
        for locator in pageLocators:
            if locatorName == locator['name']:
                return locator['locator'], locator['locateUsing']


    def getByType(self, locatorType):
        try:
            locator_type = locatorType.lower()

            if locator_type == "id":
                return MobileBy.ID
            elif locator_type == "xpath":
                return MobileBy.XPATH
            elif locator_type == "name":
                return MobileBy.NAME
            elif locator_type == "class":
                return MobileBy.CLASS_NAME
            elif locator_type == "link":
                return MobileBy.LINK_TEXT
            elif locator_type == "partiallink":
                return MobileBy.PARTIAL_LINK_TEXT
            elif locator_type == "image":
                return MobileBy.IMAGE

        except:
            self.log.error("Locator Type '" + locatorType + "' is not listed.")



    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +" and locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator +" and locatorType: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="id", element=None):
        """
        Either provide element or a combination of locator and locatorType
        """

        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("clicked on element with locator: " + locator +" locatorType: " + locatorType)
        except:
            self.log.error("cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("send data on element with locator: " + locator +" locatorType: " + locatorType)
        except:
            self.log.error("Unable to send data on the element with locator: " + locator +" locatorType: " + locatorType)
            print_stack()

    def clearKeys(self, locator="", locatorType="id", element=None):
        """
        Clear keys of an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.clear()
            self.log.info("Clear data of element with locator: " + locator +" locatorType: " + locatorType)
        except:
            self.log.error("cannot clear data of the element with locator: " + locator +" locatorType: " + locatorType)
            print_stack()

    def dropdownSelectElement(self, locator, locatorType="id", selector="", selectorType="value"):
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            if selectorType == "value":
                sel.select_by_value(selector)
                time.sleep(1)
            elif selectorType == "index":
                sel.select_by_index(selector)
                time.sleep(1)
            elif selectorType == "text":
                sel.select_by_visible_text(selector)
                time.sleep(1)
            self.log.info("Element selected with selector: " + str(selector) + " and selectorType: " + selectorType)

        except:
            self.log.error("Element not selected with selector: " + str(selector) + " and selectorType: " + selectorType)
            print_stack()

    def getDropdownOptionsCount(self, locator, locatorType="id"):
        '''
        get the number of options of drop down list
        :return: number of Options of drop down list
        '''
        options = None
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            options = sel.options
            self.log.info("Element found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator + " and locatorType: " + locatorType)

        return options

    def getDropdownSelectedOptionText(self, locator, locatorType="id"):
        '''
        get the text of selected option in drop down list
        :return: the text of selected option in drop down list
        '''
        selectedOption_text = None
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            selectedOption_text = sel.first_selected_option.text
            self.log.info("Return the selected option of drop down list with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.error("Can not return the selected option of drop down list with locator: " + locator + " and locatorType: " + locatorType)

        return selectedOption_text

    def getDropdownSelectedOptionValue(self, locator, locatorType="id"):
        '''
        get the value of selected option in drop down list
        :return: the value of selected option in drop down list
        '''
        selectedOption_value = None
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            selectedOption_value = sel.first_selected_option.get_attribute("value")
            self.log.info("Return the selected option of drop down list with locator: " + locator +" and locatorType: " + locatorType)
        except:
            self.log.error("Can not return the selected option of drop down list with locator: " + locator +" and locatorType: " + locatorType)

        return selectedOption_value



    def isElementSelected(self, locator, locatorType):
        isSelected = None
        try:
            element = self.getElement(locator, locatorType)
            isSelected = element.is_selected()
            self.log.info("Element found with locator: " + locator +" and locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator +" and locatorType: " + locatorType)

        return isSelected

    def isElementChecked(self, locator, locatorType):
        isChecked = None
        try:
            element = self.getElement(locator, locatorType)
            isChecked = element.get_attribute("checked")
            self.log.info("Element is Checked with locator: " + locator +" and locatorType: " + locatorType)
        except:
            self.log.error("Element is not Checked with locator: " + locator +" and locatorType: " + locatorType)

        return isChecked



    def getElementList(self, locator, locatorType="id"):
        """
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            #self.log.info("Element list found with locator: " + locator +" and locatorType: " + locatorType)
        except Exception as e:
            print(e)

            #self.log.error("Element list not found with locator: " + locator +" and locatorType: " + locatorType)

        return element





    def move_to_element(self, locator="", locatorType="id", element=None):
        """
        Either provide element or a combination of locator and locatorType
        """

        try:
            if locator:
                element = self.getElement(locator, locatorType)
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            time.sleep(2)
            self.log.info("hover to element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.error("cannot hover to the element with locator: " + locator +" locatorType: " + locatorType)
            print_stack()


    def move_to_element_and_click(self, locator="", locatorType="id", element=None):

        """
        This method is used when element is not receiving the direct click
        :param locator: it takes locator string as parameter
        :locatorType: it takes locator type as parameter
        :return: it returns nothing
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()
                self.log.info(
                    "Clicked on the element with locator_properties: " + locator + " and locator_type: " + locatorType)
            else:
                self.log.error("Unable to click on the element with locator_properties: " + locator + " and locator_type: " + locatorType)
        except:
            self.log.error("Exception occurred during mouse click action.")



    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) !=0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Exception occurred during text retrieval. " + info)
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        This method is used to return the boolean value for element present
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element found with locator: " + locator +" and locatorType: " + locatorType)
                return True
            else:
                self.log.error("Element not found with locator: " + locator +" and locatorType: " + locatorType)
                return False
        except:
            self.log.error("Element not found with locator: " + locator +" and locatorType: " + locatorType)
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +" and locatorType: " + locatorType)
            else:
                self.log.error("Element is not displayed with locator: " + locator +" and locatorType: " + locatorType)
            return isDisplayed
        except:
            self.log.error("Element is not displayed with locator: " + locator +" and locatorType: " + locatorType)
            return False

    def elementPresenceCheck(self, locator="", locatorType="id"):
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElementToBeClickable(self, locator, locatorType = 'id', timeout = 10, pollFrequency = 0.5 ):
        """
                This function is used for explicit waits till element clickable
                :param locator_properties: it takes locator string as parameter
                :param locator_type: it takes locator type as parameter
                :param timeout: this is the maximum time to wait for particular element
                :return: it returns the boolean value according to the element located or not
        """
        element = None
        try:
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")

            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            ByType = self.getByType(locatorType)
            element = wait.until(EC.element_to_be_clickable((ByType,locator)))

            self.log.info("Element appeared on the web page")

        except:
            self.log.error("Exception occurred while waiting for element to be clickable.")
            print_stack()

        return element

    def waitForElementToBePresent(self, locator, locatorType = 'id', timeout = 10, pollFrequency = 0.5 ):
        """
                This function is used for explicit waits till element clickable
                :param locator_properties: it takes locator string as parameter
                :param locator_type: it takes locator type as parameter
                :param timeout: this is the maximum time to wait for particular element
                :return: it returns the boolean value according to the element located or not
        """
        element = None
        try:
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be Present")

            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[StaleElementReferenceException])
            ByType = self.getByType(locatorType)
            element = wait.until(EC.presence_of_element_located((ByType,locator)))

            self.log.info("Element appeared on the web page")

        except:
            self.log.error("Exception occurred while waiting for element to be Present.")
            print_stack()

        return element


    def waitForElementToBeDisplayed(self, locator, locatorType = 'id', timeout = 10, pollFrequency = 0.5 ):
        """
                This function is used for explicit waits till element clickable
                :param locator_properties: it takes locator string as parameter
                :param locator_type: it takes locator type as parameter
                :param timeout: this is the maximum time to wait for particular element
                :return: it returns the boolean value according to the element located or not
        """
        element = None
        try:
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be displayed")

            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,ignored_exceptions=[StaleElementReferenceException])
            ByType = self.getByType(locatorType)
            element = wait.until(EC.visibility_of_element_located((ByType,locator)))

            self.log.info("Element appeared on the web page")

        except:
            self.log.error("Exception occurred while waiting for element to be visible.")
            print_stack()

        return element



    def webScroll(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")



    def getAttributeValue(self, locator="", locatorType="id", element=None, attribute=""):
        '''
        get attribute value
        '''
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            attribute_value = element.get_attribute(attribute)
        except:
            self.log.error("Failed to get " + attribute + " in element with locator: " +locator + " and locatorType: " + locatorType)
            print_stack()
            attribute_value = None
        return attribute_value


    def page_has_loaded(self):
        try:
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script('return document.readyState == "complete";'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script('return jQuery.active == 0'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script('return typeof jQuery != "undefined"'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script('return angular.element(document).injector().get("$http").pendingRequests.length === 0'))
        except:
            return False


    def verify_text_contains(self, actual_text, expected_text):

        """
        This method verifies that actual text in the expected string
        :param actual_text: it takes actual keyword/ substring
        :param expected_text: it takes the string value to search actual keyword in it
        :return: it return boolean value according to verification
        """

        self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
        self.log.info("Expected Text From Application Web UI --> :: " + expected_text)

        if expected_text.lower() in actual_text.lower():
            self.log.info("### VERIFICATION TEXT CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION TEXT DOES NOT CONTAINS !!!")
            return False

    def verify_text_match(self, actual_text, expected_text):

        """
        This method verifies the exact match of actual text and expected text
        :param actual_text: it takes actual string value
        :param expected_text: it takes the expected string value to match with
        :return: it return boolean value according to verification
        """

        self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
        self.log.info("Expected Text From Application Web UI --> :: " + expected_text)

        if expected_text.lower() == actual_text.lower():
            self.log.info("### VERIFICATION TEXT MATCHED !!!")
            return True
        else:
            self.log.error("### VERIFICATION TEXT DOES NOT MATCHED !!!")
            return False




    def take_screenshots(self, file_name_initials):

        """
        This method takes screen shot for reporting
        :param file_name_initials: it takes the initials for file name
        :return: it returns the destination directory of screenshot
        """

        file_name = file_name_initials + "." + str(round(time.time() * 1000)) + ".png"
        cur_path = os.path.abspath(os.path.dirname(__file__))
        screenshot_directory = os.path.join(cur_path, r"../Logs/Screenshots/")

        destination_directory = os.path.join(screenshot_directory, file_name)

        try:
            if not os.path.exists(screenshot_directory):
                os.makedirs(screenshot_directory)

            self.driver.save_screenshot(destination_directory)
            self.log.info("Screenshot saved to directory: " + destination_directory)
        except Exception as ex:
            self.log.error("### Exception occurred:: ", ex)
            print_stack()

        return destination_directory


    def vertical_scroll(self, scroll_view, class_name, text):
        """
        This function is used for vertical scroll
        :param scroll_view: class name for scrollView
        :param class_name: class name for text view
        :param text: text of the element
        :return: this function returns nothing
        """
        try:
            self.driver.find_element_by_android_uiautomator(
                "new UiScrollable(new UiSelector().scrollable(true)" +
                ".className(\"" + scroll_view + "\")).scrollIntoView(new UiSelector()" +
                ".className(\"" + class_name + "\").text(\"" + text + "\"))")
            self.log.info("Vertically scrolling into the view.")

        except Exception as ex:
            self.log.error("Exception occurred while vertically scrolling into the view: ", ex)


    def horizontal_scroll(self, scroll_view, class_name, text):
        """
        This function is used for horizontal scroll
        :param scroll_view: class name for scroll view
        :param class_name: class name for text view
        :param text: text of the element
        :return: this function returns nothing
        """
        try:
            self.driver.find_element_by_android_uiautomator(
                "new UiScrollable(new UiSelector().scrollable(true)" +
                ".className(\"" + scroll_view + "\")).setAsHorizontalList().scrollIntoView(new UiSelector()" +
                ".className(\"" + class_name + "\").text(\"" + text + "\"))")
            self.log.info("Horizontally scrolling into the view.")

        except Exception as ex:
            self.log.error("Exception occurred while horizontally scrolling into the view: ", ex)


    def nev_back(self):
        self.driver.back()