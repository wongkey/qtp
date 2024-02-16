# 导入tushare
import tushare as ts
# 初始化pro接口
pro = ts.pro_api('7f82a7242ba2fc55404df6c2572ccec44d7425623961120f8fed6d6b')


#日线复权
df = ts.pro_bar(ts_code='000001.SZ', adj='hfq', start_date='20240101', end_date='20240206')
print(df)
