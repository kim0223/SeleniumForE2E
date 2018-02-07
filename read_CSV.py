import csv
file_path="./testdata/"
file_name="testdata2.csv"
#取得CSV第一欄資料
testdata1 = open(file_path+file_name,"r")
text1 = csv.DictReader(testdata1)
account = [row['account'] for row in text1]
# 取得CSV第二欄資料
testdata2 = open(file_path+file_name,"r")
text2 = csv.DictReader(testdata2)
password = [row['password'] for row in text2]
# 取得CSV第三欄資料
testdata3 = open(file_path+file_name,"r")
text3 = csv.DictReader(testdata3)
type = [row['type'] for row in text3]
# 取得CSV第四欄資料
testdata4 = open(file_path+file_name,"r")
text4 = csv.DictReader(testdata4)
result = [row['result'] for row in text4]

#計算資料總行數
myfile = open(file_path+file_name,"r")
lines = len(myfile.readlines())
#輸出所有資料行
i=0
j=lines-1
while i< j:
    print(account[i],type[i],password[i],result[i])
    i += 1
