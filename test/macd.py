#计算MACD指标

def cal_macd(df,short=12,long=26,dea=9,close='收盘价_复权'):
    df['EMA short'] = df[close].ewm(span=short, adjust=False).mean()
    df['EMA long'] = df[close].ewm(span=long,adjust=False).mean()
    df['DIF'] = df['EMA short'] - df['EMA long']
    df['DEA'] = df['DIF'].ewm(span=dea,adjust=False).mean()
    df['MACD'] = (df['DIF'] - df['DEA']) *2
    del df['EMA short'], df['EMA long']
    return df

'''
# 3、计算顶底背离
cond1 = df['price_new high'] == 1
# 条件1: 在拐点处判断
cond2 = df['price new low'] == 1
cond3 = df['close'] > df['last_peak_price']
# 条件2:当前均值比上一次拐点高 (股价创新高)
cond4 = df['close'] < df['last_valley_price']
# 条件3: 当前均值比上一次拐点低 (股价创新低)
cond5 = df['DIF'] > df['last_valley _dif']
# 条件4:当前DEA比上一次拐点高 (DEA创新高)
cond6 = df['DIF'] < df['last peak dif']
# 条件5: 当前DEA比上一次拐点低 (DEA创新低)
df.loc[cond1 & cond3 & cond6,'signal'] =顶背离
df.loc[cond2 & cond4 & cond5,'signal'] =底背离
'''

