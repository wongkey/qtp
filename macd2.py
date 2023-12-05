import pandas as pd

day_list = [1,5,10,20]

# df = pd.read hdf('stock ddbl data.h5'，key='df')
df = pd.read hdf('stock ddbl data diff.h5', key='df')
start_time = '20070101'
end_time = '20210331'
df = df[df['candle end time'] >= pd.to_datetime(start_time)]
df = df[df['candle end time'] <= pd.to datetime(end time)]
for signal, group in df.groupby('signal'):
    print(' n' + str(signal))
    print(group[[str(i) + '日后涨跌幅' for i n day_list]].describe())
    for i in day_list:
        if signal =='底背离':
            print(str(i) + '天后涨跌幅大于0概率' ,'\t', float(group[groupe[]))
        if signal =='顶背离':
            print(str(i) + '天后涨跌幅小于0概率' ,'\t', float(group[group[]]))