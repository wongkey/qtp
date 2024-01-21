import akshare as ak
import pandas as pd


def get_stock_data(engine):
    conn = engine.connect()
    print("开始采集A股股票代码和简称")
    data = ak.stock_info_a_code_name()
    stock_data = pd.DataFrame({'Symbol': data['code'], 'StockName': data['name']})
    # print(stock_data)
    stock_data.to_sql(name="basic_data_stock_code", con=conn, index=False ,if_exists='replace')
    conn.commit()
    conn.close()
    print("采集A股股票代码和简称完成")