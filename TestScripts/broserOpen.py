# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import xlrd
# import time
# import re
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# import os
# from selenium.webdriver.common.keys import Keys
#
# #open cmd and run this comments:chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"
# options = Options()
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# chrome_driver = r'D:\\chromedriver\\chromedriver.exe'
# #driver = webdriver.Chrome(chrome_options=options , executable_path=chrome_driver)
# driver = webdriver.Chrome(options=options , executable_path=chrome_driver)
#
# print(driver.title)
# #//div[@class='row ng-star-inserted']/div[2]/div//ancestor::ul[@class='dotes-member-ul']/li[1]/img
#
# before_XPath = "//div[@class='row ng-star-inserted']/div["
# aftertd_XPath_1 = "]/div"
# midle_xpath="//ancestor::ul[@class='dotes-member-ul']/li["
# last_xpath="]/img"
# afterpatname="]/div//ancestor::div[@class='title']/div[1]"
#
# a=0
# totalcounts=len(driver.find_elements(By.XPATH,"//div[@class='row ng-star-inserted']/div"))
# for t_row in range(1, (totalcounts + 1)):
#     FinalXPath = before_XPath + str(t_row) + aftertd_XPath_1
#     FinalXPath2 = before_XPath + str(t_row) + afterpatname
#     cell_text = driver.find_element_by_xpath(FinalXPath2).text
#     print(cell_text)
#     #print(cell_text)
#     for t_col in range(1,4):
#         FinalXPath1 = FinalXPath+midle_xpath+str(t_col)+last_xpath

#         try:
#             t=driver.find_element_by_xpath(FinalXPath1).get_attribute('title')
#             print(t)
#         except:
#             print("...............E")
#


l=[1,2,4,5,3,32,2,3,3,5,4]
item=5

listlangth=len(l)

index=[i for i in range(listlangth) if l[i]==item]
print(f' item {item} will display in this index {index}')

