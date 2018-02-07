from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep
import unittest, time, re
#引入HTMLTestRunner包
import HTMLTestRunner
import csv
import threading
class PCHOME_LOGIN(unittest.TestCase):
    '''PChome login'''
#初始化设置
    def setUp(self):
     self.driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
     self.driver.implicitly_wait(10)
     self.verificationErrors = []
     self.accept_next_alert = True
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_case1(self):
        print("start job1:"+time.ctime())
        self.driver.get("https://www.google.com.tw/search?q=python+unittest+threading&source=lnt&tbs=lr:lang_1zh-CN%7Clang_1zh-TW&lr=lang_zh-CN%7Clang_zh-TW&sa=X&ved=0ahUKEwiBu6egoYbZAhUDfLwKHbQNBl4QpwUIHg&biw=1268&bih=568")
        time.sleep(2)
    def test_case2(self):
        print("start job2:"+time.ctime())
        self.driver.get("https://stackoverflow.com/questions/23757473/how-to-unittest-that-a-thread-is-spawned")
        time.sleep(2)

        def thread():
            print("go thread")
            # 建立執行緒陣列
            threads = []
            added_thread1 = threading.Thread(target=test_case1, name="T1")
            added_thread2 = threading.Thread(target=test_case2, name="T2")
            threads.append(added_thread1)
            threads.append(added_thread2)
            # 加入並執行執行緒
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            print("all done:" + time.ctime())
if __name__ == "__main__":
    unittest.main()
    #thread()

