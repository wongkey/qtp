import talib

import pybroker as pb
from pybroker.ext.data import AKShare

pb.param(name='stock_code', value='600000')
    
akshare = AKShare()

df = akshare.query(symbols=[pb.param(name='stock_code')], start_date='20230101', end_date='20230201')

#rsi_20 = pb.indicator('rsi_20', lambda data: talib.RSI(data.close, timeperiod=20))
#print(rsi_20(df))
df['macd'], df['macdsignal'], df['macdhist'] = talib.MACD(df.close, fastperiod=12, slowperiod=26, signalperiod=9)

df['MFI'] = talib.MFI(df.high, df.low, df.close, df.volume, timeperiod=14)

print(df['MFI'])
'''
Overlap Studies(重叠指标)
----------------------------------------------------------------------------
BBANDS               Bollinger Bands （布林带）
DEMA                 Double Exponential Moving Average （双指数移动平均线）
EMA                  Exponential Moving Average （指数移动平均线）
HT_TRENDLINE         Hilbert Transform - Instantaneous Trendline
KAMA                 Kaufman Adaptive Moving Average
MA                   Moving average（移动平均线）
MAMA                 MESA Adaptive Moving Average（自适应移动平均）
MAVP                 Moving average with variable period（变周期移动平均）
MIDPOINT             MidPoint over period
MIDPRICE             Midpoint Price over period
SAR                  Parabolic SAR
SAREXT               Parabolic SAR - Extended
SMA                  Simple Moving Average（简单移动平均线）
T3                   Triple Exponential Moving Average (T3)
TEMA                 Triple Exponential Moving Average （三重指数移动平均线）
TRIMA                Triangular Moving Average
WMA                  Weighted Moving Average（加权移动平均线）


Momentum Indicators(动量指标类)
----------------------------------------------------------------------------
ADX                  Average Directional Movement Index（平均趋向指数）
ADXR                 Average Directional Movement Index Rating
APO                  Absolute Price Oscillator
AROON                Aroon
AROONOSC             Aroon Oscillator
BOP                  Balance Of Power
CCI                  Commodity Channel Index
CMO                  Chande Momentum Oscillator
DX                   Directional Movement Index
MACD                 Moving Average Convergence/Divergence (平滑异同移动平均线)
MACDEXT              MACD with controllable MA type
MACDFIX              Moving Average Convergence/Divergence Fix 12/26
MFI                  Money Flow Index
MINUS_DI             Minus Directional Indicator
MINUS_DM             Minus Directional Movement
MOM                  Momentum
PLUS_DI              Plus Directional Indicator
PLUS_DM              Plus Directional Movement
PPO                  Percentage Price Oscillator
ROC                  Rate of change : ((price/prevPrice)-1)*100
ROCP                 Rate of change Percentage: (price-prevPrice)/prevPrice
ROCR                 Rate of change ratio: (price/prevPrice)
ROCR100              Rate of change ratio 100 scale: (price/prevPrice)*100
RSI                  Relative Strength Index （相对强弱指数）
STOCH                Stochastic
STOCHF               Stochastic Fast
STOCHRSI             Stochastic Relative Strength Index
TRIX                 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
ULTOSC               Ultimate Oscillator
WILLR                Williams' %R

'''

