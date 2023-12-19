import numpy as np
from numba import njit

from data.macd import get_data_macd

def cmma(bar_data, lookback):

    @njit  # Enable Numba JIT.
    def vec_cmma(values):
        #print(type(values))
        # Initialize the result array.
        n = len(values)
        out = np.array([np.nan for _ in range(n)])

        # For all bars starting at lookback:
        for i in range(lookback, n):
            # Calculate the moving average for the lookback.
            ma = 0
            for j in range(i - lookback, i):
                ma += values[j]
            ma /= lookback
            # Subtract the moving average from value.
            out[i] = values[i] - ma
        
        print(out)
        return out

    # Calculate with close prices.
    return vec_cmma(bar_data.close)

def macd_dif(bar_data, lookback):
    
    @njit  # Enable Numba JIT.
    def vec_macd_dif(df):
        # out = df.to_numpy()
        n = len(df)
        out = np.array([np.nan for _ in range(n)])
        
        for i, row in df.iterrows():
            #out[i]= row['DIF']
            out[i] = 0
        return out
    
    df = get_data_macd()
    print(df)
    return vec_macd_dif(df['DIF'])

def macd_dea(bar_data, lookback):
    
    @njit  # Enable Numba JIT.
    def vec_macd_dea(df):
        # out = df.to_numpy()
        n = len(df)
        print(n)
        out = np.array([np.nan for _ in range(n)])
        
        for i, row in df.iterrows():
            #out[i]= row['DEA']
            out[i] = 0
        return out
    
    df = get_data_macd()
    return vec_macd_dea(df['DEA'])

