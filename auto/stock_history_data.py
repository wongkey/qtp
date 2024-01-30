import akshare as ak
import pybroker as pb
import pandas as pd
import tushare as ts

from sqlalchemy import text

def get_stock_history_data(engine):
    
    print("开始采集股票历史数据")
    conn = engine.connect()
    sql = "SELECT * FROM basic_data_stock_code_akshare WHERE Symbol IN ('000012','000333','000623','000756','000951')"
    df = pd.read_sql(text(sql), conn)
    
    # 设置token
    ts.set_token('7f82a7242ba2fc55404df6c2572ccec44d7425623961120f8fed6d6b')
    # 初始化pro接口
    pro = ts.pro_api()
            
    # 从akshare取股票历史数据
    for index,row in df.iterrows():
        try:
            # print("股票代码：",row['Symbol'])
            symbolCode = row['Symbol']
            stockName = row['StockName']
            h_data = ak.stock_zh_a_hist(symbol=symbolCode, period="daily", start_date=pb.param(name='start_date'), end_date=pb.param(name='end_date'), adjust="hfq") #hfq 后复权数据
            #print(h_data)
            stock_zh_a_hist_df = pd.DataFrame({'date': h_data['日期'], 'symbol': symbolCode, 'stockName': stockName, 'open': h_data['开盘'], 'close':h_data['收盘'], 'high': h_data['最高'], 'low': h_data['最低'], 'volume': h_data['成交量'], 'tradingAmount': h_data['成交额'], 'swing': h_data['振幅'], 'changePercent': h_data['涨跌幅'], 'changeAmount': h_data['涨跌额'], 'turnoverRate': h_data['换手率'] })
            stock_zh_a_hist_df.to_sql(name="basic_data_stock_history", con=conn, index=False ,if_exists='append')
            conn.commit()
        except Exception as error:
            print(symbolCode, stockName, "数据采集异常", error)
        else:
            print(symbolCode, stockName,'采集完成')

    # 从tushare取股票历史数据
    for index,row in df.iterrows():    
        try:

            # 获取日线数据
            tushare_stock_data = pro.daily(ts_code='000001.sz', start_date='20180701', end_date='20180718')
            tushare_stock_data.to_sql(name="basic_data_stock_code_tushare", con=conn, index=False ,if_exists='replace')
        except Exception as error:
            print(symbolCode, stockName, "数据采集异常", error)
        else:
            print(symbolCode, stockName,'采集完成')

    print("股票历史数据采集完成")
    
