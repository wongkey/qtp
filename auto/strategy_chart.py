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
from auto.strategy_chart_kline import create_top_left
from auto.strategy_chart_table import create_table
import pandas as pd

def create_data_history_grid(df,result) -> Grid:

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
        .add(create_top_left(df,result), grid_opts=opts.GridOpts(pos_left="5%", pos_right="55%", pos_top="10%", pos_bottom="50%"))
        .add(create_top_left(df,result), grid_opts=opts.GridOpts(pos_left="55%", pos_right="5%", pos_top="10%", pos_bottom="50%"))
        .add(create_top_left(df,result), grid_opts=opts.GridOpts(pos_left="5%", pos_right="55%", pos_top="60%", pos_bottom="5%"))
        .add(create_top_left(df,result), grid_opts=opts.GridOpts(pos_left="55%", pos_right="5%", pos_top="60%", pos_bottom="5%"))
    )
    
    return grid

def create_strategy_charts(df,result):

    tab = Tab()
    tab.add(create_table('return_metrics','回测绩效'), '回测绩效')
    tab.add(create_table('return_order','订单'), '订单')
    tab.add(create_table('return_positions','持仓'), '持仓')
    tab.add(create_table('return_portfolio','投资组合'), '投资组合')
    tab.add(create_table('return_trades','交易'), '交易')
    tab.add(create_data_history_grid(df,result), '股票图表')
    
    tab.render('回测结果.html')
