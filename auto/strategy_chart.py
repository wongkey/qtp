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

def create_KLine_Chart(data,result) -> Kline:
    xdf=data[['date']]
    xdf.index=pd.to_datetime(xdf.date)
    
    ydf=data[['open','close','high','low']]
        
    all_points = result.orders[['type','date','fill_price']]
    
    buy_points = all_points[all_points['type']=='buy']
    sell_points = all_points[all_points['type']=='sell']
    
    buy_points = buy_points[['date','fill_price']]
    sell_points = sell_points[['date','fill_price']]

    buy_points['date'] = pd.to_datetime(buy_points['date'], unit='s').dt.strftime('%Y%m%d')
    sell_points['date'] = pd.to_datetime(sell_points['date'], unit='s').dt.strftime('%Y%m%d')

    buy_points = dict(zip(buy_points['date'], buy_points['fill_price']))
    sell_points = dict(zip(sell_points['date'], sell_points['fill_price']))
        
    kline = Kline(init_opts=opts.InitOpts(width='100%',height='400px'))

    kline.add_xaxis(xdf.index.strftime('%Y%m%d').tolist())
    kline.add_yaxis("kline", 
        y_axis=ydf.values.tolist(),
        markpoint_opts=opts.MarkPointOpts(
            # 标记点数据
            data=[
                *[
                # MarkPointItem：标记点数据项
                opts.MarkPointItem(
                     # 标注名称
                    name=value, 
                    type_ = None,
                    value_index = None,
                    value_dim = None,
                    coord=[day,value], 
                    value="买",
                    x = None,  #一般默认就好
                    y = None,  #一般默认就好
                    symbol = None,  #一般默认就好
                    symbol_size = None,  #一般默认就好
                    itemstyle_opts = {"color": "RED"},
                )
                for day, value in buy_points.items()
                ],
                *[
                # MarkPointItem：标记点数据项
                opts.MarkPointItem(
                     # 标注名称
                    name=value, 
                    type_ = None,
                    value_index = None,
                    value_dim = None,
                    coord=[day,value], 
                    value="卖",
                    x = None,  #一般默认就好
                    y = None,  #一般默认就好
                    symbol = None,  #一般默认就好
                    symbol_size = None,  #一般默认就好
                    itemstyle_opts = {"color": "GREEN"},
                )
                for day, value in sell_points.items()
                ],
            ],
            
            symbol = None,  #一般默认就好
            symbol_size = None,  #一般默认就好
            label_opts = opts.LabelOpts(position="inside", color="#fff"),
        ),
    )
        
    kline.set_global_opts(
            xaxis_opts=opts.AxisOpts(is_scale=True),
            yaxis_opts=opts.AxisOpts(
                is_scale=True,
                splitarea_opts=opts.SplitAreaOpts(
                    is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                ),
            ),
            datazoom_opts=[
                opts.DataZoomOpts(
                    is_show=False,
                    type_="inside",
                    xaxis_index=[0, 1],
                    range_start=0,
                    range_end=100,
                    ),
                opts.DataZoomOpts(
                    is_show=True,
                    xaxis_index=[0, 1],
                    type_="slider",
                    pos_top="85%",
                    range_start=0,
                    range_end=100,
                ),
                opts.DataZoomOpts(
                    is_show=True,
                    xaxis_index=[0, 1],
                    type_="slider",
                    pos_top="85%",
                    range_start=0,
                    range_end=100,
                ),
            ],
            title_opts=opts.TitleOpts(title="回测图表"),
            tooltip_opts=opts.TooltipOpts(
                trigger="axis",
                axis_pointer_type="cross",
                background_color="rgba(245, 245, 245, 0.8)",
                border_width=1,
                border_color="#ccc",
                textstyle_opts=opts.TextStyleOpts(color="#000"),
            ),            
        )
    #kline.render("K线图.html")
    #kline.overlap(create_MACD_Chart(data,result))
    return kline

def create_strategy_info(infoName) -> Table:
    table = Table()
    
    #数据库连接参数
    hostname = "localhost" #数据库IP
    dbname = "qtp" #数据库名
    uname = "root" #用户名
    pwd = "ASDFqwer1234" #密码

    engine = create_engine('mysql+pymysql://' + uname + ':' + pwd + '@' + hostname + '/' + dbname + '')

    conn = engine.connect()
    
    sql = "SELECT * FROM " + infoName
    df = pd.read_sql(text(sql), conn)
    
    headers = df.columns.tolist()
    rows = [list(row) for row in df.values]
    #print(headers)
    #print(rows)
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title="回测绩效")
    )
    return table

def create_data_history_grid(df,result) -> Grid:
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
        .add(create_KLine_Chart(df,result), grid_opts=opts.GridOpts(pos_left="5%", pos_right="55%", pos_top="10%", pos_bottom="50%"))
        .add(line2, grid_opts=opts.GridOpts(pos_left="55%", pos_right="5%", pos_top="10%", pos_bottom="50%"))
        .add(line3, grid_opts=opts.GridOpts(pos_left="5%", pos_right="55%", pos_top="60%", pos_bottom="5%"))
        .add(line4, grid_opts=opts.GridOpts(pos_left="55%", pos_right="5%", pos_top="60%", pos_bottom="5%"))
    )
    return grid

def create_strategy_charts(df,result,pageName):

    tab = Tab()
    tab.add(create_strategy_info('return_metrics'), "回测绩效")
    tab.add(create_strategy_info('return_order'), "订单")
    tab.add(create_strategy_info('return_positions'), "持仓")
    tab.add(create_strategy_info('return_portfolio'), "投资组合")
    tab.add(create_strategy_info('return_trades'), "交易")
    tab.add(create_data_history_grid(df,result), "股票图表")
    
    pageName = pageName + " " + "回测结果.html"
    tab.render(pageName)
