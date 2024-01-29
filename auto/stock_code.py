import akshare as ak
import tushare as ts
import pandas as pd

#分别从akshare和tushare两个数据源提取数据

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
    
    # 导入tushare库

# 设置token
ts.set_token('your token here')
# 初始化pro接口
pro = ts.pro_api()
# 获取日线数据
df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718'