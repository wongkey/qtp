import pybroker as pb
import pandas as pd
import traceback

from auto.indicator_talib import calculate_indicator
from pybroker import Strategy
from sqlalchemy import text
from auto.strategy_content import buy_with_indicator,buy_low
from auto.strategy_chart import create_strategy_charts
from auto.parameter import database

def execute_backtest():
    print("开始回测")
    
    datasource = pd.DataFrame()
    
    backtest_symbol = pb.param(name='backtest_symbol')
    backtest_start_date = pb.param(name='backtest_start_date')
    backtest_end_date = pb.param(name='backtest_end_date')
    initial_cash_value = int(pb.param(name='initial_cash'))

    print('backtest_symbol:', backtest_symbol)
    print('backtest_start_date:', backtest_start_date)
    print('backtest_end_date:', backtest_end_date)
    print('initial_cash_value:', initial_cash_value)
    
    engine = database();
    conn = engine.connect()
    sql = f"SELECT * FROM basic_data_stock_code_akshare WHERE Symbol IN ({backtest_symbol})"
    df = pd.read_sql(text(sql), conn)
    
    #初始资金
    my_config = pb.StrategyConfig(initial_cash=initial_cash_value)
    
    # 处理查询结果
    for index,row in df.iterrows():
        try:
            symbolCode = row['Symbol']
            stockName = row['StockName']
            
            pageName = symbolCode + " " +  stockName
            
            sql = f"SELECT * FROM basic_stock_history_day_hfq_akshare WHERE symbol='{symbolCode}' AND date BETWEEN '{backtest_start_date}' AND '{backtest_end_date}' ORDER BY date"
            print(sql)
            df = pd.read_sql(text(sql), conn)
            
            #计算指标
            data_with_indicator = calculate_indicator(df)
            data_with_indicator['date'] = pd.to_datetime(data_with_indicator['date'])
            
            # print(data_with_indicator.shape[0])
            datasource = pd.concat([datasource, data_with_indicator])
            # print(datasource.shape[0])
        except Exception as error:
            print(symbolCode, stockName, "回测异常", traceback.print_exc(), " : ", error)
        else:
            print(symbolCode, stockName,'回测完成')
            # print(data_with_indicator)

    #在pybroker中注册指标名称
    '''MACD指标'''
    pb.register_columns('macd')
    pb.register_columns('macdsignal')
    pb.register_columns('macdhist')

    '''MFI指标'''
    pb.register_columns('MFI')
    '''CCI指标'''
    pb.register_columns('CCI')
    '''ROC指标'''
    pb.register_columns('ROC')
    '''RSI指标'''
    pb.register_columns('RSI')
    '''OBV指标'''
    pb.register_columns('OBV')
    '''ATR指标'''
    pb.register_columns('ATR')
    
    print(datasource)
    #创建策略
    strategy = Strategy(datasource, start_date=backtest_start_date, end_date=backtest_end_date, config=my_config)
    
    # for index,row in df.iterrows():    
    # print(row['Symbol'])
    
    # 设置股票对应的策略
    strategy.add_execution(buy_low, symbols=['000012','000333','000623','000756','000951'])
    
    #strategy.add_execution(buy_with_indicator, symbols=['000012','000333','000623','000756','000951'])
    
    # 执行回测，并打印出回测结果的度量值（四舍五入到小数点后四位）
    result = strategy.backtest()
    print(result.metrics_df.round(2))
    return_order_metrics = result.metrics_df.round(2)
    
    trade_count=0
    initial_market_value=0

    for index,row in return_order_metrics.iterrows():
        name = row['name']
        value = row['value']
                
        if(name=='trade_count'): trade_count=value
        elif (name=='initial_market_value'): initial_market_value=value
        elif (name=='end_market_value'): end_market_value=value
        elif (name=='total_pnl'): total_pnl=value
        elif (name=='unrealized_pnl'): unrealized_pnl=value
        elif (name=='total_return_pct'): total_return_pct=value
        elif (name=='total_profit'): total_profit=value
        elif (name=='total_loss'): total_loss=value
        elif (name=='total_fees'): total_fees=value
        elif (name=='max_drawdown'): max_drawdown=value
        elif (name=='max_drawdown_pct'): max_drawdown_pct=value
        elif (name=='win_rate'): win_rate=value
        elif (name=='loss_rate'): loss_rate=value
        elif (name=='winning_trades'): winning_trades=value
        elif (name=='losing_trades'): losing_trades=value
        elif (name=='avg_pnl'): avg_pnl=value
        elif (name=='avg_return_pct'): avg_return_pct=value
        elif (name=='avg_trade_bars'): avg_trade_bars=value
        elif (name=='avg_profit'): avg_profit=value
        elif (name=='avg_profit_pct'): avg_profit_pct=value
        elif (name=='avg_winning_trade_bars'): avg_winning_trade_bars=value
        elif (name=='avg_loss'): avg_loss=value
        elif (name=='avg_loss_pct'): avg_loss_pct=value
        elif (name=='avg_losing_trade_bars'): avg_losing_trade_bars=value
        elif (name=='largest_win'): largest_win=value
        elif (name=='largest_win_pct'): largest_win_pct=value
        elif (name=='largest_win_bars'): largest_win_bars=value
        elif (name=='largest_loss'): largest_loss=value
        elif (name=='largest_loss_pct'): largest_loss_pct=value
        elif (name=='largest_loss_bars'): largest_loss_bars=value
        elif (name=='max_wins'): max_wins=value
        elif (name=='max_losses'): max_losses=value
        elif (name=='sharpe'): sharpe=value
        elif (name=='sortino'): sortino=value
        elif (name=='profit_factor'): profit_factor=value
        elif (name=='ulcer_index'): ulcer_index=value
        elif (name=='upi'): upi=value
        elif (name=='equity_r2'): equity_r2=value
        elif (name=='std_error'): std_error=value
          
    insertsql = text("INSERT INTO return_metrics (trade_count, initial_market_value, end_market_value, total_pnl, unrealized_pnl, total_return_pct, total_profit, total_loss, total_fees, max_drawdown, max_drawdown_pct, win_rate, loss_rate, winning_trades, losing_trades, avg_pnl, avg_return_pct, avg_trade_bars, avg_profit, avg_profit_pct, avg_winning_trade_bars, avg_loss, avg_loss_pct, avg_losing_trade_bars, largest_win, largest_win_pct, largest_win_bars, largest_loss, largest_loss_pct, largest_loss_bars, max_wins, max_losses, sharpe, sortino, profit_factor, ulcer_index, upi, equity_r2, std_error) VALUES (" 
                              + " " + str(trade_count) 
                              + ", " + str(initial_market_value) 
                              + ", " + str(end_market_value) 
                              + ", " + str(total_pnl) 
                              + ", " + str(unrealized_pnl) 
                              + ", " + str(total_return_pct) 
                              + ", " + str(total_profit) 
                              + ", " + str(total_loss) 
                              + ", " + str(total_fees) 
                              + ", " + str(max_drawdown) 
                              + ", " + str(max_drawdown_pct) 
                              + ", " + str(win_rate) 
                              + ", " + str(loss_rate) 
                              + ", " + str(winning_trades) 
                              + ", " + str(losing_trades) 
                              + ", " + str(avg_pnl) 
                              + ", " + str(avg_return_pct) 
                              + ", " + str(avg_trade_bars) 
                              + ", " + str(avg_profit) 
                              + ", " + str(avg_profit_pct) 
                              + ", " + str(avg_winning_trade_bars) 
                              + ", " + str(avg_loss) 
                              + ", " + str(avg_loss_pct) 
                              + ", " + str(avg_losing_trade_bars) 
                              + ", " + str(largest_win) 
                              + ", " + str(largest_win_pct) 
                              + ", " + str(largest_win_bars) 
                              + ", " + str(largest_loss) 
                              + ", " + str(largest_loss_pct) 
                              + ", " + str(largest_loss_bars) 
                              + ", " + str(max_wins) 
                              + ", " + str(max_losses) 
                              + ", " + str(sharpe) 
                              + ", " + str(sortino) 
                              + ", " + str(profit_factor) 
                              + ", " + str(ulcer_index) 
                              + ", " + str(upi) 
                              + ", " + str(equity_r2)                             
                              + ", " + str(std_error) + ")")
                
    conn.execute(insertsql)
    conn.commit()

    # 显示所有列
    pd.set_option('display.max_columns',None)
    # 显示所有行
    pd.set_option('display.max_rows',None)

    return_order_df = result.orders
    return_order_df.to_sql(name="return_order", con=conn, index=True ,if_exists='append')
    conn.commit()
    print(return_order_df)
    
    return_positions_df = result.positions
    return_positions_df.to_sql(name="return_positions", con=conn, index=True ,if_exists='append')
    conn.commit()
    print(return_positions_df)

    return_portfolio_df = result.portfolio
    return_portfolio_df.to_sql(name="return_portfolio", con=conn, index=True ,if_exists='append')
    conn.commit()
    print(return_portfolio_df)
        
    return_trades_df = result.trades
    return_trades_df.to_sql(name="return_trades", con=conn, index=True ,if_exists='append')
    conn.commit()
    print(return_trades_df)   
  
    #创建图表
    create_strategy_charts(data_with_indicator,result)