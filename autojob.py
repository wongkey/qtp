import schedule
import time

from auto.parameter import get_init_parameters
from auto.clear_data import clear_backtest_data
from auto.backtest import execute_backtest

#自动启动时间
startTime = "17:52"

def job():
    print("开始自动执行程序")
    
    #获取公共参数
    get_init_parameters()
    
    #清除数据
    clear_backtest_data()
    
    #回测
    execute_backtest()

job()

# 设置每天的特定时间执行任务（此处为每天上午10点）
# schedule.every().day.at(startTime).do(job)

# while True:
    # 运行所有已安排的作业并等待下次调度
#    schedule.run_pending()
#    time.sleep(1)