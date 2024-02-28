# -*- coding: utf-8 -*-
"""
图表函数
"""

from pyecharts import options as opts
from pyecharts.charts import Kline,Page,Grid,Bar,Line,Tab
from pyecharts.components import Table
from pyecharts.globals import ThemeType
from sqlalchemy import create_engine,text
from pyecharts.faker import Faker

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

def create_grid(result) -> Grid:
    line1 = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("A", Faker.values())
        .add_yaxis("B", Faker.values())
    )

    line2 = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("C", Faker.values())
        .add_yaxis("D", Faker.values())
    )
    
    line3 = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("E", Faker.values())
        .add_yaxis("F", Faker.values())
    )

    line4 = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("G", Faker.values())
        .add_yaxis("H", Faker.values())
    )

    grid = (
        Grid(init_opts=opts.InitOpts(width="100%", height="800px"))
        .add(line1, grid_opts=opts.GridOpts(pos_left="5%", pos_right="55%", pos_top="10%", pos_bottom="50%"))
        .add(line2, grid_opts=opts.GridOpts(pos_left="55%", pos_right="5%", pos_top="10%", pos_bottom="50%"))
        .add(line3, grid_opts=opts.GridOpts(pos_left="5%", pos_right="55%", pos_top="60%", pos_bottom="5%"))
        .add(line4, grid_opts=opts.GridOpts(pos_left="55%", pos_right="5%", pos_top="60%", pos_bottom="5%"))
    )
    return grid

    
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
tab.add(create_grid(df), "周")
tab.add(create_strategy_info(df), "月")
tab.add(create_strategy_info(df), "季")
tab.add(create_strategy_info(df), "年")
tab.add(create_strategy_info(df), "1分")
tab.add(create_strategy_info(df), "5分")
tab.add(create_strategy_info(df), "15分")
tab.add(create_strategy_info(df), "30分")
tab.add(create_strategy_info(df), "60分")

tab.render("可视化界面.html")

line1 = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis("A", Faker.values())
    .add_yaxis("B", Faker.values())
)

line2 = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis("C", Faker.values())
    .add_yaxis("D", Faker.values())
)
line3 = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis("E", Faker.values())
    .add_yaxis("F", Faker.values())
)
line4 = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis("G", Faker.values())
    .add_yaxis("H", Faker.values())
)

grid = (
    Grid(init_opts=opts.InitOpts(width="100%", height="800px"))
    .add(line1, grid_opts=opts.GridOpts(pos_left="5%", pos_right="55%", pos_top="10%", pos_bottom="50%"))
    .add(line2, grid_opts=opts.GridOpts(pos_left="55%", pos_right="5%", pos_top="10%", pos_bottom="50%"))
    .add(line3, grid_opts=opts.GridOpts(pos_left="5%", pos_right="55%", pos_top="60%", pos_bottom="5%"))
    .add(line4, grid_opts=opts.GridOpts(pos_left="55%", pos_right="5%", pos_top="60%", pos_bottom="5%"))
    .render("grid_test.html")
)
