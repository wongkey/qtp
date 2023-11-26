# coding=UTF-8
import urllib.request
import pymysql
import sys
import json

#获取沪深两市全部股票代码
url='https://api.biyingapi.com/zs/hfsjy/603237/dn/108658639b4e045982'
# print(url)
response = urllib.request.urlopen(url)
returnStr = response.read().decode("UTF-8")
response.close();

data = json.loads(returnStr)

try:
    db = pymysql.connect(host="localhost",user="root",password="ASDFqwer1234",database="qtp")

except Exception as e:
    print('Error when Connection to DB.' + str(e))
    sys.exit()
    
cursor = db.cursor()

'''
字段名称	数据类型	字段说明
d	string	交易时间，短分时级别格式为yyyy-MM-dd HH:mm:ss，日线级别为yyyy-MM-dd
o	number	开盘价（元）
h	number	最高价（元）
l	number	最低价（元）
c	number	收盘价（元）
v	number	成交量（手）
e	number	成交额（元）
zf	number	振幅（%）
hs	number	换手率（%）
zd	number	涨跌幅（%）
zde	number	涨跌额（元）
'''

for item in data:
    insertSql = "INSERT INTO `qtp`.`basic_data_stock_history` (`TimeKey`,`Symbol`,`StockName`,`Open`,`Close`,`High`,`Low`,`TradingVolume`,`TradingAmount`,`Swing`,`ChangePercent`,`ChangeAmount`,`TurnoverRate`) VALUES ('" + str(item['d']) + "','603237',''," + item['o'] + "," + item['c'] + "," + item['h'] + "," + item['l'] + "," + item['v'] + "," + item['e'] + "," + item['zf'] + "," + item['hs'] + "," + item['zde'] + "," + item['zd'] + ");"
    cursor.execute(insertSql)

#print(response.read().decode("UTF-8"))

db.commit()
cursor.close()
db.close()