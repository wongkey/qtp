import pymysql
import pandas as pd
import sys
from sqlalchemy import create_engine

def calculate_macd(data, short_period=12, long_period=26, signal_period=9):
    """
    计算MACD指标和信号线
    参数：
    data: 包含价格数据的DataFrame，需包含'Close'列
    short_period: 快线的计算周期，默认为12
    long_period: 慢线的计算周期，默认为26
    signal_period: 信号线的计算周期，默认为9
    返回：
    DataFrame，包含'MACD'和'Signal'列
    """
    close_prices = data['close']
    
    # 计算快线和慢线
    ema_short = close_prices.ewm(span=short_period, adjust=False).mean()
    ema_long = close_prices.ewm(span=long_period, adjust=False).mean()
    
    # 计算MACD和信号线
    macd = ema_short - ema_long
    signal = macd.ewm(span=signal_period, adjust=False).mean()
    
    macd_data = pd.DataFrame({'date': data['date'], 'symbol': data['symbol'],'open': data['open'],'close': data['close'],'high': data['high'],'low': data['low'], 'DIF': macd, 'DEA': signal})
    macd_data['date'] = pd.to_datetime(macd_data['date'])
    
    return macd_data

def save_data_macd(macd_data):    
    engine = create_engine('mysql+pymysql://root:ASDFqwer1234@localhost/qtp')
    conn = engine.connect()
    
    macd_data.to_sql(name="calculate_data_macd", con=conn, if_exists='replace')
    # macd_data.to_sql('calculate_data_macd', con=db, if_exists='replace', index=False)
    
    # 提交更改并关闭连接
    #conn.commit()
    #conn.close()

def get_data_macd():    
    try:
        db = pymysql.connect(host="localhost",user="root",password="ASDFqwer1234",database="qtp")

    except Exception as e:
        print('Error when Connection to DB.' + str(e))
        sys.exit()

    query = "SELECT * FROM calculate_data_macd ORDER BY TimeKey"
    # query = "SELECT * FROM calculate_data_macd WHERE Symbol='603237' ORDER BY TimeKey"
    df = pd.read_sql(query, db)
    db.commit()
    db.close()
    return df
    