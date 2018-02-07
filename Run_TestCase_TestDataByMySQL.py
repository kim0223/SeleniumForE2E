import  unittest, time
from HTMLTestRunner import HTMLTestRunner

#設定測試路徑
test_dir='./testcase'
#選擇測試檔案
discover = unittest.defaultTestLoader.discover(test_dir,pattern ='verify_by_mysql.py')

if __name__ == "__main__":

#建立測試報告
    now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
    filename="./testresult/"+now+"_result.html"
    fp=open(filename,'wb')
    runner = HTMLTestRunner(stream = fp, title = now+u"TestReoprt", description = u"sanity test")
    runner.run(discover)
    fp.close()