# -*- coding: utf-8 -*-
#引入webdriver和unittest所需要的包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
#引入HTMLTestRunner包
import HTMLTestRunner 
class Baidu2(unittest.TestCase):
    '''奇摩搜尋2222'''
#初始化设置
    def setUp(self):
     self.driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
     self.driver.implicitly_wait(10)
     self.verificationErrors = []
     self.accept_next_alert = True#百度搜索用例

    def test_case1(self):
        '''新聞驗證1'''
        driver = self.driver
        driver.get("https://tw.yahoo.com/")
        driver.find_element_by_link_text(u"娛樂").click()
        self.assertEqual(u"Yahoo奇摩新聞2", driver.title)


def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()