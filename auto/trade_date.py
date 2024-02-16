import akshare as ak
import tushare as ts
import pandas as pd
import pybroker as pb

def get_trade_date(engine):
    try:
        conn = engine.connect()
        
        print("开始从tushare采集交易日期") 
        
        ts.set_token(pb.param(name='tushare_token'))
        
        first_processing_date = pb.param(name='first_processing_date')
        last_processing_date = pb.param(name='last_processing_date')
        
        #tushare初始化
        pro = ts.pro_api()
        #查询当前所有正常上市交易的股票列表
        tushare_trade_date = pro.trade_cal(exchange='', start_date=first_processing_date, end_date=last_processing_date)
        tushare_trade_date.to_sql(name="basic_trade_date_tushare", con=conn, index=False ,if_exists='append')
        
        conn.commit()
    
    except Exception as error:
        print('从tushare采集交易日期错误：', error)
    else:
        print("从tushare采集交易日期完成")