import pybroker as pb
from pybroker import Strategy
from pybroker.ext.data import AKShare

from strategy.strategy_content import buy_with_stop_loss

from strategy.strategy_chart import create_strategy_charts

def create_strategy():
    # 定义全局参数 "stock_code"（股票代码）、"percent"（持仓百分比）和 "stop_profit_pct"（止盈百分比）
    pb.param(name='stock_code', value='600000')
    pb.param(name='percent', value=1)
    pb.param(name='stop_loss_pct', value=10)
    pb.param(name='stop_profit_pct', value=10)

    akshare = AKShare()

    df = akshare.query(symbols=[pb.param(name='stock_code')], start_date='20200131', end_date='20230228')
#    print(df)
    
    # 创建策略配置，初始资金为 500000
    my_config = pb.StrategyConfig(initial_cash=500000)
    # 使用配置、数据源、起始日期、结束日期，以及刚才定义的交易策略创建策略对象
    strategy = Strategy(akshare, start_date='20200131', end_date='20230228', config=my_config)
    # 添加执行策略，设置股票代码和要执行的函数
    strategy.add_execution(fn=buy_with_stop_loss, symbols=[pb.param(name='stock_code')])
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

    create_strategy_charts(df,result)

    return result