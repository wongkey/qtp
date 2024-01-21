import akshare as ak
import pybroker as pb
import pandas as pd

from sqlalchemy import create_engine, text

def get_stock_history_data(engine):
    
    print("开始采集股票历史数据")
    conn = engine.connect()
    sql = "SELECT * FROM basic_data_stock_code"
    df = pd.read_sql(text(sql), conn)

    # 处理查询结果
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
        
    print("股票历史数据采集完成")