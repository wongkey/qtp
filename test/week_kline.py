import pandas as pd

from pybroker.ext.data import AKShare
from pyecharts import options as opts
from pyecharts.charts import Kline

akshare = AKShare()
df = akshare.query(symbols='600000', start_date='20230101', end_date='20231223')
print(df)

# 将交易日期字符串变为日期类型
df['date'] = pd.to_datetime(df['date'])  
# 将日期列设为索引
df.set_index('date', inplace = True)

def transfer_price_freq(data, time_freq):
    """
    将数据转化为指定周期：开盘价(周期第一天)、收盘价(周期最后一天)、最高价(周期)、最低价(周期)
    :param data:日数据，包含每天开盘价、收盘价、最高价、最低价
    :param time_freq: 转换周期,周：‘W’，月:‘M’
    :return:
    """
    df_trans = pd.DataFrame()
    df_trans['open'] = data['open'].resample(time_freq).first()
    df_trans['close'] = data['close'].resample(time_freq).last()
    df_trans['high'] = data['high'].resample(time_freq).max()
    df_trans['low'] = data['low'].resample(time_freq).min()
    return df_trans

def create_KLine_Chart(data) -> Kline:
    xdf=data[['date']]
    xdf.index=pd.to_datetime(xdf.date)
    
    ydf=data[['open','close','high','low']]
        
    kline = Kline(init_opts=opts.InitOpts(width='100%',height='400px'))

    kline.add_xaxis(xdf.index.strftime('%Y%m%d').tolist())
    kline.add_yaxis("kline", 
        y_axis=ydf.values.tolist()
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
            title_opts=opts.TitleOpts(title="图表"),
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

# 我们传入df，及"M"参数即可得到月K数据
month_df = transfer_price_freq(df, 'M')
month_df['date'] = month_df.index

week_df = transfer_price_freq(df, 'W')
week_df['date'] = week_df.index

#print(transfer_df)

create_KLine_Chart(week_df).render("周K线.html")
create_KLine_Chart(month_df).render("月K线.html")

