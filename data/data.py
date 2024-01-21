import pymysql
import pandas as pd
import sys
from sqlalchemy import create_engine
import akshare as ak
from pybroker.ext.data import AKShare
import pybroker as pb

def get_stock_code_and_name():
    
    akshare = AKShare()
    df = akshare.query(symbols=['000001'], start_date='20230101', end_date='20231231')
    print(df)

    # data = ak.stock_info_a_code_name()
    # print(data) 
    
    # stock_data = pd.DataFrame({'Symbol': data['code'], 'StockName': data['name']})
    # print(stock_data)

    #engine = create_engine('mysql+pymysql://root:ASDFqwer1234@localhost/qtp')
    #conn = engine.connect()

    # stock_data.to_sql(name="basic_data_stock_code", con=conn, index=False ,if_exists='replace')
    # conn.commit()
    
    # h_data = ak.stock_zh_a_hist(symbol='000001', period="daily", start_date="20230101", end_date='20231231', adjust="hfq")
    # print(h_data)
    
    # stock_zh_a_hist_df = pd.DataFrame({'date': h_data['日期'], 'symbol': h_data['name']})
    # print(stock_zh_a_hist_df)
    # stock_zh_a_hist_df.to_sql(name="basic_data_stock_history", con=conn, index=False ,if_exists='replace')
    # conn.commit()
    
get_stock_code_and_name()