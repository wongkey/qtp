from sqlalchemy import create_engine
from auto.parameter import get_init_parameters,last_update_data_date
from auto.trade_date import get_trade_date

from auto.clear_data import clear_basic_data
from auto.clear_data import clear_backtest_data

from auto.stock_code import get_stock_code
from auto.stock_data import get_stock_data

#数据库连接参数
hostname = "localhost" #数据库IP
dbname = "qtp" #数据库名
uname = "root" #用户名
pwd = "ASDFqwer1234" #密码

print("开始采集初始化数据程序")
engine = create_engine('mysql+pymysql://' + uname + ':' + pwd + '@' + hostname + '/' + dbname + '', future=True)

#获取公共参数
get_init_parameters(engine)

#清除基础数据
clear_basic_data(engine)

#清除回测数据
clear_backtest_data(engine)

#开始采集A股股票代码和简称
get_stock_code(engine)

#开始采集A股交易日期
get_trade_date(engine)

#开始采集A股股票历史数据
get_stock_data(engine)

#更新数据截至日期
last_update_data_date(engine)

print("完成采集初始化数据程序")