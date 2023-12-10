from pyecharts import options as opts
from pyecharts.charts import Kline,Page,Grid,Bar
from pyecharts.components import Table
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

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
        
    kline = Kline(init_opts=opts.InitOpts(width='100%',height='700px'))

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
                    range_start=98,
                    range_end=100,
                    ),
                opts.DataZoomOpts(
                    is_show=True,
                    xaxis_index=[0, 1],
                    type_="slider",
                    pos_top="85%",
                    range_start=98,
                    range_end=100,
                ),
            ],
            title_opts=opts.TitleOpts(title="回测图表"),
        )
    #kline.render("K线图.html")
    return kline

def create_strategy_bar(data,result) -> Bar:
    xdf=data[['date']]
    xdf.index=pd.to_datetime(xdf.date)
    
#    all_points = result.portfolio[['date','cash','equity','pnl']]
#    all_points['date'] = pd.to_datetime(all_points['date'], unit='s').dt.strftime('%Y%m%d')
#    all_points = dict(zip(all_points['date'], all_points['cash']))
    
    ydf=result.portfolio[['pnl']]
    
#    y=[88, 102, 47, 107, 130, 31, 58]

    buy_points = {"周二": 0, "周三": 100}

    bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    bar.add_xaxis(xdf.index.strftime('%Y%m%d').tolist())
    bar.add_yaxis(
            "收益(Profit & Loss)",
            ydf.pnl.tolist(),
            # MarkPointOpts：标记点配置项
            markpoint_opts=opts.MarkPointOpts(
                # 标记点数据
                data=[
                    *[
                    # MarkPointItem：标记点数据项
                    opts.MarkPointItem(
                         # 标注名称
                        name="自定义标记点", 
                        type_ = None,
                        value_index = None,
                        value_dim = None,
                        coord=[day,value], #这里是直角坐标系x轴第三个，y轴第三个
                        value=value,
                        x = None,  #一般默认就好
                        y = None,  #一般默认就好
                        symbol = None,  #一般默认就好
                        symbol_size = None,  #一般默认就好
                        itemstyle_opts = None,
                    )
                    for day, value in buy_points.items()
                    ],
                ],
                
                symbol = None,  #一般默认就好
                symbol_size = None,  #一般默认就好
                label_opts = opts.LabelOpts(position="inside", color="#fff"),          
            ),
        )
    #bar.add_yaxis("商家B", Faker.values())
    bar.set_global_opts(
        title_opts=opts.TitleOpts(title=""),
        legend_opts=opts.LegendOpts(
            type_='plain',
            selected_mode=True,
            is_show=False,
            pos_left=None,
            pos_right=None,
            pos_top=None,
            pos_bottom=None,
            orient='horizontal',
            align='auto',
            padding=5,
            item_gap=10,
            item_width=25,
            item_height=14,
            inactive_color='#ccc',
            textstyle_opts=None,
            legend_icon=None
        ), 
    )
    bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False)) #不显示标签
    #bar.render("bar_markpoint_custom.html")
    return bar

def create_strategy_info(result) -> Table:
    table = Table()
    
    metrics = result.metrics_df.round(2)
    
    headers = metrics.columns.tolist()
    rows = [list(row) for row in metrics.values]
    #print(headers)
    #print(rows)
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title="回测绩效")
    )
    return table

def create_strategy_charts(df,result):
    grid_chart = Grid(
        init_opts=opts.InitOpts(
            width="100%",
            height="800px",
            animation_opts=opts.AnimationOpts(animation=False),
        )
    )
    grid_chart.add(
        create_KLine_Chart(df,result),
        grid_opts=opts.GridOpts(pos_left="5%", pos_right="5%", height="50%"),
    )

    grid_chart.add(
        create_strategy_bar(df,result),
        grid_opts=opts.GridOpts(pos_left="5%", pos_right="5%", pos_top="63%", height="16%"),
    )
    
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        grid_chart,
        create_strategy_info(result),
    )
    page.render("K线图.html")