#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep
import unittest, time, re
import MySQLdb
#引入HTMLTestRunner包
import HTMLTestRunner

class PCHOME_LOGIN(unittest.TestCase):
    '''PChome login'''
#初始化设置
    def setUp(self):
     self.driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
     self.driver.implicitly_wait(10)
     self.verificationErrors = []
     self.accept_next_alert = True
    
    def test_case1(self):
        #執行測試腳本
        driver = self.driver
        driver.get("https://buzzorange.com/techorange/2017/08/29/lindy-on-programming/")
        title=driver.find_element_by_class_name('entry-title').text
        print(title)
        # 連接 MySQL 資料庫
        db = MySQLdb.connect(host="localhost",
                             user="root", passwd="1qaz2wsx", db="sakila", charset='utf8')
        cursor = db.cursor()
        # 執行 MySQL 查詢指令
        cursor.execute("select * from city where city_id=601")

        # 取回所有查詢結果
        results = cursor.fetchall()
        for record in results:
            col1 = record[0]
            col2 = record[1]
            print(col2)
            self.assertEqual(title, col2)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    unittest.main()
    main()
