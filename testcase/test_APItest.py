    import unittest, time, re
    import requests
    import csv
    class APItest(unittest.TestCase):
        '''APItest'''
    #初始化设置
        def setUp(self):
            self.verificationErrors = []
            print()
        def test_case1(self):
            '''Google API TEST'''
            # 取得CSV第一欄資料
            testdata1 = open("C:/Users/kim/AppData/Local/Programs/Python/Python36-32/testdata/APIlist.csv","r")
            text1 = csv.DictReader(testdata1)
            API_list = [row['APIlist'] for row in text1]
            # 取得CSV總筆數
            filename = "C:/Users/kim/AppData/Local/Programs/Python/Python36-32/testdata/APIlist.csv"
            myfile = open(filename)
            lines = len(myfile.readlines())
            # 執行測試腳本
            i = 0
            j = lines - 1
            while i < j:
                r3 = requests.get(API_list[i])
                if r3.status_code !=200:
                    print(API_list[i]+" :"+"API Testing Fail")
                else:
                    print(API_list[i]+" :"+"API Testing Success")
                i += 1
        def tearDown(self):
            self.assertEqual([], self.verificationErrors)
    if __name__ == "__main__":
         unittest.main()
