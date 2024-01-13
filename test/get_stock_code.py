# coding=UTF-8
import urllib.request
import pymysql
import sys
import json

#获取沪深两市全部股票代码
url='http://api.biyingapi.com/hslt/list/108658639b4e045982'
# print(url)
response = urllib.request.urlopen(url)
returnStr = response.read().decode("UTF-8")
response.close();

data = json.loads(returnStr)
print(data)

try:
    db = pymysql.connect(host="localhost",user="root",password="ASDFqwer1234",database="qtp")

except Exception as e:
    print('Error when Connection to DB.' + str(e))
    sys.exit()
    
cursor = db.cursor()

# for item in data:
#    insertSql = "INSERT INTO `qtp`.`basic_data_stock_code`(`Symbol`,`StockName`,`Exchange`) VALUES ('" + str(item['dm']) + "','" + str(item['mc']) + "','" + str(item['jys']) + "');"
#    cursor.execute(insertSql)
    # print(str(item['dm']) + " | " + str(item['mc']) + " | " + str(item['jys']))

#print(response.read().decode("UTF-8"))

db.commit()
cursor.close()
db.close()