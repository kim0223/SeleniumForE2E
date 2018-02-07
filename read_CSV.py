import csv
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
password = [row['type'] for row in text3]
# 取得CSV第四欄資料
testdata4 = open("C:/Users/kim/AppData/Local/Programs/Python/Python36-32/testdata/testdata2.csv", "r")
text4 = csv.DictReader(testdata4)
password = [row['result'] for row in text4]
testdata1 = open("testdata/testdata2.csv", "r")
text = csv.DictReader(testdata1)
account = [row['account'] for row in text]
testdata2 = open("testdata/testdata2.csv", "r")
text2 = csv.DictReader(testdata2)
password = [row['password'] for row in text2]
filename = "testdata/testdata2.csv"
myfile = open(filename)
lines = len(myfile.readlines())
i=0
j=lines-1
while i< lines:
    i+=1
print(i,account[2],password[1])
#print(lines)