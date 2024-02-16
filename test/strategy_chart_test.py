# -*- coding: utf-8 -*-
"""
图表函数
"""

from pyecharts import options as opts
from pyecharts.charts import Kline,Page,Grid,Bar,Line,Tab
from pyecharts.components import Table
from pyecharts.globals import ThemeType
from sqlalchemy import create_engine,text

import pandas as pd

def create_KLine_Chart(result) -> Kline:        
    kline = Kline(init_opts=opts.InitOpts(width='100%',height='400px'))


    #kline.render("K线图.html")
    #kline.overlap(create_MACD_Chart(data,result))
    return kline

def create_strategy_info(result) -> Table:
    table = Table()
        
    headers = result.columns.tolist()
    rows = [list(row) for row in result.values]
    #print(headers)
    #print(rows)
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title="回测绩效")
    )
    return table

#数据库连接参数
hostname = "localhost" #数据库IP
dbname = "qtp" #数据库名
uname = "root" #用户名
pwd = "ASDFqwer1234" #密码

engine = create_engine('mysql+pymysql://' + uname + ':' + pwd + '@' + hostname + '/' + dbname + '')

conn = engine.connect()

sql = "SELECT * FROM return_metrics"
df = pd.read_sql(text(sql), conn)

tab = Tab()
tab.add(create_strategy_info(df), "分时")
tab.add(create_KLine_Chart(df), "日")
tab.add(create_strategy_info(df), "周")
tab.add(create_strategy_info(df), "月")
tab.add(create_strategy_info(df), "季")
tab.add(create_strategy_info(df), "年")
tab.add(create_strategy_info(df), "1分")
tab.add(create_strategy_info(df), "5分")
tab.add(create_strategy_info(df), "15分")
tab.add(create_strategy_info(df), "30分")
tab.add(create_strategy_info(df), "60分")

tab.render("可视化界面.html")