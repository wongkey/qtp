import schedule
import time


 
def job():
    print("采集A股股票代码和简称")

    
    print("采集股票数据")
 
# 设置每天的特定时间执行任务（此处为每天上午10点）
schedule.every().day.at("15:30").do(job)

while True:
    print("开始自动执行程序")
    # 运行所有已安排的作业并等待下次调度
    schedule.run_pending()
    time.sleep(1)