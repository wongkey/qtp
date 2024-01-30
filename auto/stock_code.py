import akshare as ak
import tushare as ts
import pandas as pd
import pybroker as pb
#分别从akshare和tushare两个数据源提取数据，然后进行比较，如相同则视为数据有效。

def get_stock_data(engine):
    try:
        conn = engine.connect()

        print("开始从akshare采集A股股票代码和简称")    
        data = ak.stock_info_a_code_name()
        akshare_stock_data = pd.DataFrame({'Symbol': data['code'], 'StockName': data['name']})
        # print(stock_data)
        akshare_stock_data.to_sql(name="basic_data_stock_code_akshare", con=conn, index=False ,if_exists='replace')
        conn.commit()

        print("开始从akshare采集A股股票代码和简称")
        #设置token
        ts.set_token(pb.param(name='tushare_token'))
        #ts.set_token('7f82a7242ba2fc55404df6c2572ccec44d7425623961120f8fed6d6b')
        #tushare初始化
        pro = ts.pro_api()
        #查询当前所有正常上市交易的股票列表
        tushare_stock_data = pro.stock_basic(exchange='', list_status='L')
        tushare_stock_data.to_sql(name="basic_data_stock_code_tushare", con=conn, index=False ,if_exists='replace')
        conn.commit()
    
    except Exception as error:
        print('采集数据错误：', error)
    else:
        print("采集A股股票代码和简称完成")