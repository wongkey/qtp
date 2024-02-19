#import tushare as ts

#import time

import datetime

current_date = datetime.date.today()
formatted_date = current_date.strftime("%Y%m%d")

print(formatted_date)

# 初始化pro接口
# ts.set_token('b179cffec140bc54a588dc96451ebff5146896dbbc5ea6b309ab6303')

# pro = ts.pro_api('b179cffec140bc54a588dc96451ebff5146896dbbc5ea6b309ab6303')

# 接口名称：pro_bar
# 更新时间：股票和指数通常在15点～17点之间，数字货币实时更新，具体请参考各接口文档明细。
# 描述：目前整合了股票（未复权、前复权、后复权）、指数、数字货币、ETF基金、期货、期权的行情数据，未来还将整合包括外汇在内的所有交易行情数据，同时提供分钟数据。不同数据对应不同的积分要求，具体请参阅每类数据的文档说明。
# 其它：由于本接口是集成接口，在SDK层做了一些逻辑处理，目前暂时没法用http的方式调取通用行情接口。用户可以访问Tushare的Github，查看源代码完成类似功能。

# ts_code         str	Y	证券代码，不支持多值输入，多值输入获取结果会有重复记录
# start_date      str	N	开始日期 (日线格式：YYYYMMDD，提取分钟数据请用2019-09-01 09:00:00这种格式)
# end_date	      str	N	结束日期 (日线格式：YYYYMMDD)
# asset	          str	Y	资产类别：E股票 I沪深指数 C数字货币 FT期货 FD基金 O期权 CB可转债（v1.2.39），默认E
# adj	          str	N	复权类型(只针对股票)：None未复权 qfq前复权 hfq后复权 , 默认None，目前只支持日线复权，同时复权机制是根据设定的end_date参数动态复权，采用分红再投模式，具体请参考常见问题列表里的说明，如果获取跟行情软件一致的复权行情，可以参阅股票技术因子接口。
# freq	          str	Y	数据频度 ：支持分钟(min)/日(D)/周(W)/月(M)K线，其中1min表示1分钟（类推1/5/15/30/60分钟） ，默认D。对于分钟数据有600积分用户可以试用（请求2次），正式权限可以参考权限列表说明 ，使用方法请参考股票分钟使用方法。
# ma	              list  N	均线，支持任意合理int数值。注：均线是动态计算，要设置一定时间范围才能获得相应的均线，比如5日均线，开始和结束日期参数跨度必须要超过5日。目前只支持单一个股票提取均线，即需要输入ts_code参数。e.g: ma_5表示5日均价，ma_v_5表示5日均量
# factors         list	N	股票因子（asset='E'有效）支持 tor换手率 vr量比
# adjfactor       str	N	复权因子，在复权数据时，如果此参数为True，返回的数据中则带复权因子，默认为False。 该功能从1.2.33版本开始生效


# print("日数据")
# df = ts.pro_bar(ts_code='000001.SZ', freq="D", adj='qfq', start_date='20240101', end_date='20240131')
# print(df)
# time.sleep(70)

# print("周数据")
# df = ts.pro_bar(ts_code='000001.SZ', freq="W", start_date='20240101', end_date='20240131')
# print(df)
# time.sleep(70)

# print("月数据")
# df = ts.pro_bar(ts_code='000001.SZ', freq="M", start_date='20240101', end_date='20240131')
# print(df)
# time.sleep(70)

# print("1分钟数据")
# df = ts.pro_bar(ts_code='000001.SZ', freq="1min", start_date='20240101', end_date='20240131')
# print(df)
# time.sleep(70)

# print("5分钟数据")
# df = ts.pro_bar(ts_code='000001.SZ', freq="5min", start_date='20240101', end_date='20240131')
# print(df)
# time.sleep(70)

# print("15分钟数据")
# df = ts.pro_bar(ts_code='000001.SZ', freq="15min", start_date='20240101', end_date='20240131')
# print(df)
# time.sleep(70)

# print("30分钟数据")
# df = ts.pro_bar(ts_code='000001.SZ', freq="30min", start_date='20240101', end_date='20240131')
# print(df)
# time.sleep(70)

# print("60分钟数据")
# df = ts.pro_bar(ts_code='600000.SH', freq="60min", start_date='2020-01-07 09:00:00', end_date='2020-01-08 17:00:00')
# print(df)
