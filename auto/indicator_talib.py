# -*- coding: utf-8 -*-
"""
指标计算函数 （使用ta-lib包计算各类指标的函数）
"""

import talib
import pandas as pd
import pybroker as pb
from pybroker.ext.data import AKShare

def calculate_indicator(df) :
    df['macd'], df['macdsignal'], df['macdhist'] = talib.MACD(df.close, fastperiod=12, slowperiod=26, signalperiod=9)

    df['MFI'] = talib.MFI(df.high, df.low, df.close, df.volume, timeperiod=14) 
    
    # CCI 性质:自身带有一个crossover的属性，此刻因为除以了std，因此不仅符号有意义，信号本身的数值也有意义了。
    # 正常情况下这个数字在正负100之间波动。
    df['CCI'] = talib.CCI(df.high, df.low, df.close, timeperiod=14)
    
    # ROC 代表当前收盘价比之前的收盘价高百分比多少
    # 当N-day ROC 是正的时候，买入
    # 当ROC是负的时候，卖出
    df['ROC'] = talib.ROC(df.close, timeperiod=14)
    
    # RSI 如果RIS（timeperiod=14），超过70则买超，当低于30则卖超；
    # 当RSI（timeperiod=4），则超过75是超买，低于25时超卖。如果出现市场新高，但是RSI出现背离，那么就是一个reversal signal。
    df['RSI'] = talib.RSI(df.close, timeperiod=14)
    
    #RSI + OBV
    
    # OBV
    df['OBV'] = talib.OBV(df.close, df.volume)
    
    #ATR
    df['ATR'] = talib.ATR(df.high, df.low, df.close, timeperiod=14)
    
    
    
    return df
    
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