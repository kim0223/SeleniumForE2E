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


    def test_case1(self):
        '''登入驗證1'''
        #取得CSV第一欄資料
        testdata1 = open("C:/Users/kim/AppData/Local/Programs/Python/Python36-32/testdata/testdata2.csv","r")
        text1 = csv.DictReader(testdata1)
        account = [row['account'] for row in text1]
        # 取得CSV第二欄資料
        testdata2 = open("C:/Users/kim/AppData/Local/Programs/Python/Python36-32/testdata/testdata2.csv","r")
        text2 = csv.DictReader(testdata2)
        password = [row['password'] for row in text2]
        # 取得CSV第三欄資料
        testdata3 = open("C:/Users/kim/AppData/Local/Programs/Python/Python36-32/testdata/testdata2.csv", "r")
        text3 = csv.DictReader(testdata3)
        type = [row['type'] for row in text3]
        # 取得CSV第四欄資料
        testdata4 = open("C:/Users/kim/AppData/Local/Programs/Python/Python36-32/testdata/testdata2.csv", "r")
        text4 = csv.DictReader(testdata4)
        result = [row['result'] for row in text4]
        # 取得CSV總筆數
        filename = "C:/Users/kim/AppData/Local/Programs/Python/Python36-32/testdata/testdata2.csv"
        myfile = open(filename)
        lines = len(myfile.readlines())
        now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
        #取得腳本開始時間
        now2 = time.strftime("%H%M%S", time.localtime())
        #testreport對齊用
        print()
        #執行測試腳本
        i = 0
        j = lines - 1
        while i < j:
            try:
                case_item="Case"+str(i)+":"+account[i]
                print(case_item)
                driver = self.driver
                driver.get("https://www.mobile01.com/login.php?link=%2Ftopicdetail.php%3Ff%3D132%26t%3D5371462")
                driver.find_element_by_name('login_email').send_keys(account[i])
                sleep(2)
                driver.find_element_by_name('login_password').send_keys(password[i])
                sleep(2)
            #driver.find_element_by_class_name('recaptcha-checkbox-checkmark').click()
            #sleep(2)
                driver.find_element_by_name('submit_btn').click()
                sleep(3)
                if type[i] =='pass':
                    self.assertEqual("pass", result[i])
                    # 計算腳本結束時間
                    now5 = time.strftime("%H%M%S", time.localtime())
                    spend_time = int(now5) - int(now2)
                    print("spend_time:" + str(spend_time) + "s")
                else:
                    assert_text=driver.find_element_by_class_name('item-text').text
                    self.assertEqual(assert_text,result[i])
                    # 計算腳本結束時間
                    now3 = time.strftime("%H%M%S", time.localtime())
                    spend_time = int(now3) - int(now2)
                    print("spend_time:" + str(spend_time) + "s")
                i += 1
            except :
                # 截圖
                screenshot_path = "./testScreenshot/TeseCase_" + \
                                  password[i] + "_" + now + "_screenshot.png"
                driver.save_screenshot(screenshot_path)
                print("Result:FAIL Attached:"+screenshot_path)
                # 計算腳本結束時間
                now4 = time.strftime("%H%M%S", time.localtime())
                spend_time = int(now4) - int(now2)
                print("spend_time:" + str(spend_time) + "s")
                i += 1
    def test_case2(self):
        '''登入驗證1'''
        #取得CSV第一欄資料
        testdata1 = open("C:/Users/kim/AppData/Local/Programs/Python/Python36-32/testdata/testdata2.csv","r")
        text1 = csv.DictReader(testdata1)
        account = [row['account'] for row in text1]
        # 取得CSV第二欄資料
        testdata2 = open("C:/Users/kim/AppData/Local/Programs/Python/Python36-32/testdata/testdata2.csv","r")
        text2 = csv.DictReader(testdata2)
        password = [row['password'] for row in text2]
        # 取得CSV第三欄資料
        testdata3 = open("C:/Users/kim/AppData/Local/Programs/Python/Python36-32/testdata/testdata2.csv", "r")
        text3 = csv.DictReader(testdata3)
        type = [row['type'] for row in text3]
        # 取得CSV第四欄資料
        testdata4 = open("C:/Users/kim/AppData/Local/Programs/Python/Python36-32/testdata/testdata2.csv", "r")
        text4 = csv.DictReader(testdata4)
        result = [row['result'] for row in text4]
        # 取得CSV總筆數
        filename = "C:/Users/kim/AppData/Local/Programs/Python/Python36-32/testdata/testdata2.csv"
        myfile = open(filename)
        lines = len(myfile.readlines())
        now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
        #取得腳本開始時間
        now2 = time.strftime("%H%M%S", time.localtime())
        #testreport對齊用
        print()
        #執行測試腳本
        i = 0
        j = lines - 1
        while i < j:
            try:
                case_item="Case"+str(i)+":"+account[i]
                print(case_item)
                driver = self.driver
                driver.get("https://www.mobile01.com/login.php?link=%2Ftopicdetail.php%3Ff%3D132%26t%3D5371462")
                driver.find_element_by_name('login_email').send_keys(account[i])
                sleep(2)
                driver.find_element_by_name('login_password').send_keys(password[i])
                sleep(2)
            #driver.find_element_by_class_name('recaptcha-checkbox-checkmark').click()
            #sleep(2)
                driver.find_element_by_name('submit_btn').click()
                sleep(3)
                if type[i] =='pass':
                    self.assertEqual("pass", result[i])
                    # 計算腳本結束時間
                    now5 = time.strftime("%H%M%S", time.localtime())
                    spend_time = int(now5) - int(now2)
                    print("spend_time:" + str(spend_time) + "s")
                else:
                    assert_text=driver.find_element_by_class_name('item-text').text
                    self.assertEqual(assert_text,result[i])
                    # 計算腳本結束時間
                    now3 = time.strftime("%H%M%S", time.localtime())
                    spend_time = int(now3) - int(now2)
                    print("spend_time:" + str(spend_time) + "s")
                i += 1
            except :
                # 截圖
                screenshot_path = "./testScreenshot/TeseCase_" + \
                                  password[i] + "_" + now + "_screenshot.png"
                driver.save_screenshot(screenshot_path)
                print("Result:FAIL Attached:"+screenshot_path)
                # 計算腳本結束時間
                now4 = time.strftime("%H%M%S", time.localtime())
                spend_time = int(now4) - int(now2)
                print("spend_time:" + str(spend_time) + "s")
                i += 1

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        testdata.close()
        testdata2.close()
def main():
    #建立執行緒陣列
    threads=[]
    added_thread1 = threading.Thread(target=test_case1, name="T1")
    added_thread2 = threading.Thread(target=test_case2, name="T2")
    threads.append(added_thread1)
    threads.append(added_thread2)
    # 加入並執行執行緒
    for t in threads:
        t.start()
    for t in threads:
        t.join()
if __name__ == "__main__":
    unittest.main()
    main()
