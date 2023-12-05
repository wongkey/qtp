import pandas as pd
# import numpy as np

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
    close_prices = data['Close']
    
    # 计算快线和慢线
    ema_short = close_prices.ewm(span=short_period, adjust=False).mean()
    ema_long = close_prices.ewm(span=long_period, adjust=False).mean()
    
    # 计算MACD和信号线
    macd = ema_short - ema_long
    signal = macd.ewm(span=signal_period, adjust=False).mean()
    
    macd_data = pd.DataFrame({'MACD': macd, 'Signal': signal})
    return macd_data

# 示例用法
# 读取价格数据，假设数据存储在名为'data.csv'的CSV文件中
data = pd.read_csv('data.csv')

# 计算MACD指标和信号线
macd_data = calculate_macd(data)

# 打印计算结果
print(macd_data)