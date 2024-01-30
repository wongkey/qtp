import schedule
import time
import pybroker as pb
from sqlalchemy import create_engine
from auto.clear_data import clear_data
from auto.stock_code import get_stock_data
from auto.stock_history_data import get_stock_history_data
from auto.backtest import execute_backtest

#自动启动时间
startTime = "19:33"

#数据库连接参数
hostname = "localhost" #数据库IP
dbname = "qtp" #数据库名
uname = "root" #用户名
pwd = "ASDFqwer1234" #密码

# 设置tushare的token
pb.param(name='tushare_token', value='7f82a7242ba2fc55404df6c2572ccec44d7425623961120f8fed6d6b')

# 定义全局参数 "stock_code"（股票代码）
pb.param(name='stock_code', value='600000') 
# 定义全局参数 "start_date" 开始日期
pb.param(name='start_date', value='20230101') 
# 定义全局参数 "end_date" 结束日期
pb.param(name='end_date', value='20240130') 
    
# 定义全局参数 "percent"（持仓百分比） 1代表100% 0.25代表25%
pb.param(name='percent', value=0.25)
# 定义全局参数 "stop_loss_pct"（止损百分比）
pb.param(name='stop_loss_pct', value=10)
# 定义全局参数 "stop_profit_pct"（止盈百分比）
pb.param(name='stop_profit_pct', value=10)

# 创建策略配置，初始资金为 500000
my_config = pb.StrategyConfig(initial_cash=500000)

def job():
    print("开始自动执行程序")
    engine = create_engine('mysql+pymysql://' + uname + ':' + pwd + '@' + hostname + '/' + dbname + '')
    
    #清除数据
    clear_data(engine)
    
    #开始采集A股股票代码和简称
    get_stock_data(engine)
    
    #开始采集A股股票历史数据
    get_stock_history_data(engine)
    
    #回测
    execute_backtest(engine)
    
# 设置每天的特定时间执行任务（此处为每天上午10点）
schedule.every().day.at(startTime).do(job)

while True:
    # 运行所有已安排的作业并等待下次调度
    schedule.run_pending()
    time.sleep(1)