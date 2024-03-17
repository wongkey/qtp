# -*- coding: utf-8 -*-
"""
图表函数 表格
"""

from pyecharts import options as opts
from pyecharts.charts import Kline,Page,Grid,Bar,Line,Tab
from pyecharts.components import Table
from pyecharts.globals import ThemeType
from sqlalchemy import create_engine,text
from pyecharts.faker import Faker
from auto.parameter import database
import pandas as pd

def create_table(infoName,tableTitle) -> Table:
    table = Table()
    
    engine = database();
    conn = engine.connect()
    
    sql = "SELECT * FROM " + infoName
    df = pd.read_sql(text(sql), conn)
    
    headers = df.columns.tolist()
    rows = [list(row) for row in df.values]
    #print(headers)
    #print(rows)
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title=tableTitle)
    )
    return table