import logging

from selenium.webdriver import ActionChains

from SupportLibraries.base_helpers import BaseHelpers
import FrameworkUtilities.logger_utility as log_utils
import time
from appium.webdriver.common.touch_action import TouchAction


class loanRequest(BaseHelpers):
    """This class defines the method and element identifications for main page."""

    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.loginPage_locators = self.pageLocators('LoanRequest')



    def verify_SelectProductAmount(self):
        time.sleep(5)
        self.waitForElementToBeDisplayed(*self.locator(self.loginPage_locators, 'AmountBorrowText'))
        s=self.getText(*self.locator(self.loginPage_locators, 'AmountBorrowText'))

        self.log.info(type(s))
        self.log.info(s)
        time.sleep(5)
        time.sleep(5)
        self.elementClick(*self.locator(self.loginPage_locators, 'ChoosetheAmountBox'))
        time.sleep(5)

        amount = self.getElementList(*self.locator(self.loginPage_locators, 'listAmount'))
        # #year_list =self.driver.find_elements_by_xpath("//android.widget.TextView[@resource-id='android:id/text1']")
        count = len(amount)
        self.log.info(count)
        for x in amount:
            if x.text=="1000":
                x.click()
                break

        time.sleep(5)

        self.elementClick(*self.locator(self.loginPage_locators, 'ChooseMonthTenure'))
        time.sleep(5)
        tenure = self.getElementList(*self.locator(self.loginPage_locators, 'listTenure'))
        for x in tenure:
            if x.text == "30 + 90 Days":
                x.click()
                break

        time.sleep(10)
        self.driver.swipe(663, 1565, 470, 660, 985)
        time.sleep(5)
        self.elementClick(*self.locator(self.loginPage_locators, 'RequestLoanButton'))
        time.sleep(5)
        self.elementClick(*self.locator(self.loginPage_locators, 'BankAccount'))
        time.sleep(5)
        SelectBank = self.getElementList(*self.locator(self.loginPage_locators, 'SelectBankAccount'))
        count = len(SelectBank)
        self.log.info(SelectBank)
        for x in SelectBank:
            x.click()
            break
        time.sleep(5)

        self.elementClick(*self.locator(self.loginPage_locators, 'SelfDeclarationCheckBox'))
        time.sleep(5)
        self.elementClick(*self.locator(self.loginPage_locators, 'ConfirmButton'))
        time.sleep(5)
        useMoney = self.getElementList(*self.locator(self.loginPage_locators, 'UseMoneyFor'))
        count = len(useMoney)
        self.log.info(count)
        for x in useMoney:
            if x.text == "Mobile Recharge":
                x.click()
                break

        time.sleep(5)

        self.elementClick(*self.locator(self.loginPage_locators, 'continueButton'))
        time.sleep(5)

        agreeToterms = self.getElementList(*self.locator(self.loginPage_locators, 'AgreeToTerms'))
        count = len(agreeToterms)
        self.log.info(agreeToterms)
        for x in agreeToterms:
            x.click()

        time.sleep(5)
        self.elementClick(*self.locator(self.loginPage_locators, 'IAgreeButton'))
        time.sleep(10)
        self.waitForElementToBeClickable(*self.locator(self.loginPage_locators, 'VewContractButton'))
        self.elementClick(*self.locator(self.loginPage_locators, 'VewContractButton'))
        time.sleep(5)
        self.waitForElementToBeClickable(*self.locator(self.loginPage_locators, 'LoanAgreeButton'))

        self.elementClick(*self.locator(self.loginPage_locators, 'LoanAgreeButton'))
        time.sleep(5)
        self.waitForElementToBeClickable(*self.locator(self.loginPage_locators, 'LoanGotItButton'))
        self.elementClick(*self.locator(self.loginPage_locators, 'LoanGotItButton'))
        time.sleep(5)
















