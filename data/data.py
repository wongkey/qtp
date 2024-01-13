import pymysql
import pandas as pd
import sys
from sqlalchemy import create_engine
import akshare as ak
import pandas as pd

def get_stock_code_and_name():
    data = ak.stock_info_a_code_name()
    #print(data) 
    
    stock_data = pd.DataFrame({'Symbol': data['code'], 'StockName': data['name']})
    print(stock_data)
    
    hostname = "localhost"
    dbname = "qtp"
    uname = "root"
    pwd = "ASDFqwer1234"

    engine = create_engine('mysql+pymysql://root:ASDFqwer1234@localhost/qtp')
    conn = engine.connect()

    stock_data.to_sql(name="basic_data_stock_code", con=conn, index=False ,if_exists='replace')
    conn.commit()
    
get_stock_code_and_name()