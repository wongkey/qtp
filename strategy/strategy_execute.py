import pybroker as pb
from pybroker import Strategy
from pybroker import IndicatorSet

from pybroker.ext.data import AKShare

from strategy.strategy_content import buy_with_stop_loss
from strategy.strategy_content import buy_low
from strategy.strategy_content import buy_with_indicator
from strategy.strategy_content import buy_with_macd

from strategy.strategy_chart import create_strategy_charts

from indicator.indicator_content import cmma

from indicator.indicator_content import macd_dif
from indicator.indicator_content import macd_dea

from data.macd import calculate_macd
from data.macd import save_data_macd
from data.macd import get_data_macd

import pandas as pd

def create_strategy():
    # 定义全局参数 "stock_code"（股票代码）
    pb.param(name='stock_code', value='600000')
    # 定义全局参数 "percent"（持仓百分比）
    pb.param(name='percent', value=1)
    # "stop_loss_pct"（止损百分比）
    pb.param(name='stop_loss_pct', value=10)
    # "stop_profit_pct"（止盈百分比）
    pb.param(name='stop_profit_pct', value=10)

    akshare = AKShare()

    df = akshare.query(symbols=[pb.param(name='stock_code')], start_date='20210101', end_date='20230201')
    
    print(df)
    
    #计算MACD参数
    macd_data = calculate_macd(df)
    #存入数据库
    save_data_macd(macd_data)
    
    # 创建策略配置，初始资金为 500000
    my_config = pb.StrategyConfig(initial_cash=500000)
    # 使用配置、数据源、起始日期、结束日期，以及刚才定义的交易策略创建策略对象
    #strategy = Strategy(akshare, start_date='20230101', end_date='20230201', config=my_config)
    # 添加执行策略，设置股票代码和要执行的函数

    pb.register_columns('DIF')
    pb.register_columns('DEA')
    strategy = Strategy(macd_data, start_date='20210101', end_date='20230201', config=my_config)
    strategy.add_execution(buy_with_macd, symbols=[pb.param(name='stock_code')])
    
    #strategy.add_execution(fn=buy_with_stop_loss, symbols=[pb.param(name='stock_code')])
    #strategy.add_execution(fn=buy_low, symbols=[pb.param(name='stock_code')])
    #strategy.add_execution(fn=buy_with_indicator, symbols=[pb.param(name='stock_code')])
    #cmma_20 = pb.indicator('cmma_20', cmma, lookback=20)
    #strategy.add_execution(buy_with_indicator, symbols=[pb.param(name='stock_code')], indicators=cmma_20)

    #i_macd_dif = pb.indicator('macd_dif', macd_dif, lookback=0)
    #i_macd_dea = pb.indicator('macd_dea', macd_dea, lookback=0)
    
    #indicator_set = IndicatorSet()
    #indicator_set.add(i_macd_dif, i_macd_dea)
    #indicator_set(df)

    #strategy.add_execution(buy_with_macd, symbols=[pb.param(name='stock_code')], indicators=get_data_macd())
    
    # 执行回测，并打印出回测结果的度量值（四舍五入到小数点后四位）
    result = strategy.backtest()
    print('======查看绩效==========================')
    print(result.metrics_df.round(2))
    print('======查看订单==========================')
    print(result.orders)
    print('======查看持仓==========================')
    print(result.positions)
    print('======查看投资组合==========================')
    print(result.portfolio)
    print('======查看交易==========================')
    print(result.trades)    

    create_strategy_charts(macd_data,result)

    return result