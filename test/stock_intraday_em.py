# -*- coding: utf-8 -*-
"""
分时图
生成分时图时不能使用代理网络
"""

#import pandas as pd
import akshare as ak
from pyecharts import options as opts
from pyecharts.charts import Line,Grid,Bar

stock_intraday_sina_df = ak.stock_intraday_sina(symbol="sh600000", date="20231222")
print(stock_intraday_sina_df)

def create_intraday_Chart(data) -> Grid:
    xdf=data['ticktime']
    ydf_price=data['price']
    ydf_vplume=data['volume']
    #print(xdf.values.tolist())
    #print(ydf.values.tolist())
    
    line1 = (
        Line()
        .add_xaxis(xdf.values.tolist())
        .add_yaxis(
            series_name="价格", 
            y_axis=ydf_price.values.tolist(),
            symbol_size=1,
            is_hover_animation=False,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=1.5),
            #is_smooth=True,
            )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="分时图", subtitle="数据来源搜狐网", pos_left="center"
            ),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),

            yaxis_opts=opts.AxisOpts(
                min_ = data['price'].min(),  # 设置 Y 轴的最小值
                max_ = data['price'].max()  # 设置 Y 轴的最大值
            ),
            axispointer_opts=opts.AxisPointerOpts(
                is_show=True, link=[{"xAxisIndex": "all"}]
            ),
            datazoom_opts=[
                opts.DataZoomOpts(
                    is_show=True,
                    is_realtime=True,
                    start_value=0,
                    end_value=100,
                    xaxis_index=[0, 1],
                )
            ],
            xaxis_opts=opts.AxisOpts(
                type_="category",
                boundary_gap=False,
                axisline_opts=opts.AxisLineOpts(is_on_zero=True),
            ),
            legend_opts=opts.LegendOpts(pos_left="left"),
            toolbox_opts=opts.ToolboxOpts(
                is_show=True,
                feature={
                    "dataZoom": {"yAxisIndex": "none"},
                    "restore": {},
                    "saveAsImage": {},
                },
            ),
        )
    )

    bar2 = (
        Bar()
        .add_xaxis(xdf.values.tolist())
        .add_yaxis(
            series_name="成交量", 
            y_axis=ydf_vplume.values.tolist(),
            xaxis_index=1,
            yaxis_index=1,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            axispointer_opts=opts.AxisPointerOpts(
                is_show=True, link=[{"xAxisIndex": "all"}]
            ),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            xaxis_opts=opts.AxisOpts(
                grid_index=1,
                type_="category",
                boundary_gap=False,
                axisline_opts=opts.AxisLineOpts(is_on_zero=True),
                position="top",
            ),
            datazoom_opts=[
                opts.DataZoomOpts(
                    is_realtime=True,
                    type_="inside",
                    start_value=0,
                    end_value=100,
                    xaxis_index=[0, 1],
                )
            ],
            legend_opts=opts.LegendOpts(pos_left="7%"),
        )
    )
    (
        Grid(init_opts=opts.InitOpts(width="1024px", height="768px"))
        .add(chart=line1, grid_opts=opts.GridOpts(pos_left=50, pos_right=50, height="35%"))
        .add(chart=bar2, grid_opts=opts.GridOpts(pos_left=50, pos_right=50, pos_top="55%", height="35%"))
        .render("分时图.html")
    )
    return Grid

create_intraday_Chart(stock_intraday_sina_df)