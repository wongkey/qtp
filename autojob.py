import schedule
import time
from sqlalchemy import create_engine
from auto.clear_data import clear_backtest_data
from auto.parameter import get_backtest_parameters
from auto.backtest import execute_backtest

#自动启动时间
startTime = "17:52"

#数据库连接参数
hostname = "localhost" #数据库IP
dbname = "qtp" #数据库名
uname = "root" #用户名
pwd = "ASDFqwer1234" #密码

def job():
    print("开始自动执行程序")
    engine = create_engine('mysql+pymysql://' + uname + ':' + pwd + '@' + hostname + '/' + dbname + '')
    
    #获取公共参数
    get_backtest_parameters(engine)
    
    #清除数据
    clear_backtest_data(engine)
    
    #回测
    execute_backtest(engine)

job()

# 设置每天的特定时间执行任务（此处为每天上午10点）
# schedule.every().day.at(startTime).do(job)

# while True:
    # 运行所有已安排的作业并等待下次调度
#    schedule.run_pending()
#    time.sleep(1)