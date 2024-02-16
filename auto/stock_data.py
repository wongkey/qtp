import akshare as ak
import pybroker as pb
import pandas as pd
import tushare as ts

from sqlalchemy import text

def get_stock_data(engine):
    
    print("开始采集股票历史数据")
    conn = engine.connect()
    
    backtest_symbol = pb.param(name='backtest_symbol')
    sql = f"SELECT * FROM basic_data_stock_code_tushare WHERE symbol IN ({backtest_symbol})"
    df = pd.read_sql(text(sql), conn)
    
    # 初始化tushare接口
    ts.set_token(pb.param(name='tushare_token'))
    pro = ts.pro_api()
    
    # 从akshare取股票历史数据
    for index,row in df.iterrows():
        try:
            tscode = row['ts_code']
            symbolCode = row['symbol']
            stockName = row['name']
            
            #akshare 日线(不复权)
            h_data = ak.stock_zh_a_hist(symbol=symbolCode, period="daily", start_date=pb.param(name='first_processing_date'), end_date=pb.param(name='last_processing_date')) #不复权数据
            akshare_stock_data_day_bfq = pd.DataFrame({'date': h_data['日期'], 'symbol': symbolCode, 'stockName': stockName, 'open': h_data['开盘'], 'close':h_data['收盘'], 'high': h_data['最高'], 'low': h_data['最低'], 'volume': h_data['成交量'], 'tradingAmount': h_data['成交额'], 'swing': h_data['振幅'], 'changePercent': h_data['涨跌幅'], 'changeAmount': h_data['涨跌额'], 'turnoverRate': h_data['换手率'] })
            akshare_stock_data_day_bfq.to_sql(name="basic_stock_history_day_bfq_akshare", con=conn, index=False ,if_exists='append')
            conn.commit()
            
            #akshare 日线(前复权)
            h_data = ak.stock_zh_a_hist(symbol=symbolCode, period="daily", start_date=pb.param(name='first_processing_date'), end_date=pb.param(name='last_processing_date'), adjust="qfq") #qfq 前复权数据
            akshare_stock_data_day_qfq = pd.DataFrame({'date': h_data['日期'], 'symbol': symbolCode, 'stockName': stockName, 'open': h_data['开盘'], 'close':h_data['收盘'], 'high': h_data['最高'], 'low': h_data['最低'], 'volume': h_data['成交量'], 'tradingAmount': h_data['成交额'], 'swing': h_data['振幅'], 'changePercent': h_data['涨跌幅'], 'changeAmount': h_data['涨跌额'], 'turnoverRate': h_data['换手率'] })
            akshare_stock_data_day_qfq.to_sql(name="basic_stock_history_day_qfq_akshare", con=conn, index=False ,if_exists='append')
            conn.commit()

            #akshare 日线(后复权)
            h_data = ak.stock_zh_a_hist(symbol=symbolCode, period="daily", start_date=pb.param(name='first_processing_date'), end_date=pb.param(name='last_processing_date'), adjust="hfq") #hfq 后复权数据
            akshare_stock_data_day_hfq = pd.DataFrame({'date': h_data['日期'], 'symbol': symbolCode, 'stockName': stockName, 'open': h_data['开盘'], 'close':h_data['收盘'], 'high': h_data['最高'], 'low': h_data['最低'], 'volume': h_data['成交量'], 'tradingAmount': h_data['成交额'], 'swing': h_data['振幅'], 'changePercent': h_data['涨跌幅'], 'changeAmount': h_data['涨跌额'], 'turnoverRate': h_data['换手率'] })
            akshare_stock_data_day_hfq.to_sql(name="basic_stock_history_day_hfq_akshare", con=conn, index=False ,if_exists='append')
            conn.commit()
            
            #tushare 日线(不复权)
            tushare_stock_data_day_bfq = pro.daily(ts_code=tscode, start_date=pb.param(name='first_processing_date'), end_date=pb.param(name='last_processing_date'))
            tushare_stock_data_day_bfq.to_sql(name="basic_stock_history_day_bfq_tushare", con=conn, index=False ,if_exists='append')

            #tushare 日线(前复权)
            tushare_stock_data_day_qfq = pro.daily(ts_code=tscode, adj='qfq', start_date=pb.param(name='first_processing_date'), end_date=pb.param(name='last_processing_date'))
            tushare_stock_data_day_qfq.to_sql(name="basic_stock_history_day_qfq_tushare", con=conn, index=False ,if_exists='append')

            #tushare 日线(后复权)
            tushare_stock_data_day_hfq = pro.daily(ts_code=tscode, adj='hfq', start_date=pb.param(name='first_processing_date'), end_date=pb.param(name='last_processing_date'))
            tushare_stock_data_day_hfq.to_sql(name="basic_stock_history_day_hfq_tushare", con=conn, index=False ,if_exists='append')
            
            #tushare 特色数据，全部包括（不复权、前复权、后复权及各种指标）
            tushare_stock_data = pro.stk_factor(ts_code=tscode, start_date=pb.param(name='first_processing_date'), end_date=pb.param(name='last_processing_date'))
            tushare_stock_data.to_sql(name="basic_stock_history_all_tushare", con=conn, index=False ,if_exists='append')
            conn.commit()
            
            
        except Exception as error:
            print(symbolCode, stockName, "数据采集异常", error)
        else:
            print(symbolCode, stockName,'采集完成')

    print("股票历史数据采集完成")