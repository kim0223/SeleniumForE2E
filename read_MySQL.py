# -*- coding: utf-8 -*-

# 引入 MySQLdb 模組，提供連接 MySQL 的功能
import MySQLdb
SQL_command="select * from city where city_id=601"
# 連接 MySQL 資料庫
db = MySQLdb.connect(host="localhost",
    user="root", passwd="1qaz2wsx", db="sakila", charset='utf8')
cursor = db.cursor()

# 執行 MySQL 查詢指令
cursor.execute(SQL_command)

# 取回所有查詢結果
results = cursor.fetchall()

# 輸出結果
for record in results:
  col1 = record[0]
  col2 = record[1]
  print ("%s, %s" % (col1, col2))
# 關閉連線
db.close()
