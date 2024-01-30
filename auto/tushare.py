# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:58:44 2024

@author: 24313
"""

import tushare as ts


pro = ts.pro_api()

#查询当前所有正常上市交易的股票列表

data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

print(data)

# 设置token
ts.set_token('7f82a7242ba2fc55404df6c2572ccec44d7425623961120f8fed6d6b')
# 初始化pro接口
pro = ts.pro_api()
# 获取日线数据
df = pro.daily(ts_code='000001.sz', start_date='20180701', end_date='20180718')

print(df)


# 股票基本数据
df = pro.stock_basic(**{
    "ts_code": "",
    "name": "",
    "exchange": "",
    "market": "",
    "is_hs": "",
    "list_status": "L",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "symbol",
    "name",
    "area",
    "industry",
    "market",
    "list_date"
])
print(df)

# 取交易日历
# 拉取数据
df = pro.trade_cal(**{
    "exchange": "",
    "cal_date": "",
    "start_date": 20240101,
    "end_date": 20241231,
    "is_open": "",
    "limit": "",
    "offset": ""
}, fields=[
    "exchange",
    "cal_date",
    "is_open",
    "pretrade_date"
])
print(df)

        