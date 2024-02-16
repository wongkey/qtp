from sqlalchemy import text
import pandas as pd
import pybroker as pb

def get_init_parameters(engine):
    try:
        print('开始取公共参数')
        conn = engine.connect()

        sql = "SELECT * FROM parameter"
        df = pd.read_sql(text(sql), conn)
        
        tushare_token_value = df[df['paraName'] == 'tushare_token']['paraValue'].values
        first_processing_date_df = df[df['paraName'] == 'first_processing_date']['paraValue'].values
        first_processing_date_value = ''.join(first_processing_date_df)
        last_processing_date_df = df[df['paraName'] == 'last_processing_date']['paraValue'].values
        last_processing_date_value = ''.join(last_processing_date_df)
        
        backtest_symbol_df = df[df['paraName'] == 'backtest_symbol']['paraValue'].values
        backtest_symbol_value = ''.join(backtest_symbol_df)
        
        # 定义全局变量
        pb.param(name='tushare_token', value=tushare_token_value)
        pb.param(name='first_processing_date', value=first_processing_date_value)
        pb.param(name='last_processing_date', value=last_processing_date_value)
        pb.param(name='backtest_symbol', value=backtest_symbol_value)
        
        print('全局变量 tushare_token：', pb.param(name='tushare_token'))
        print('全局变量 first_processing_date', pb.param(name='first_processing_date'))
        print('全局变量 last_processing_date', pb.param(name='last_processing_date'))
        print('全局变量 backtest_symbol', pb.param(name='backtest_symbol'))

    except Exception as error:
        print('获取公共参数错误：', error)
    else:
        print('获取公共参数完成')
        

def get_backtest_parameters(engine):
    try:
        print('开始取公共参数')
        conn = engine.connect()

        sql = "SELECT * FROM parameter"
        df = pd.read_sql(text(sql), conn)
        
        backtest_symbol_df = df[df['paraName'] == 'backtest_symbol']['paraValue'].values
        backtest_symbol_value = ''.join(backtest_symbol_df)
        backtest_start_date_df = df[df['paraName'] == 'backtest_start_date']['paraValue'].values
        backtest_start_date_value = ''.join(backtest_start_date_df)
        backtest_end_date_df = df[df['paraName'] == 'backtest_end_date']['paraValue'].values
        backtest_end_date_df_value = ''.join(backtest_end_date_df)
        
        percent_df = df[df['paraName'] == 'percent']['paraValue'].values
        percent_value = ''.join(percent_df)
        stop_loss_pct_df = df[df['paraName'] == 'stop_loss_pct']['paraValue'].values
        stop_loss_pct_value = ''.join(stop_loss_pct_df)
        stop_profit_pct_df = df[df['paraName'] == 'stop_profit_pct_df']['paraValue'].values
        stop_profit_pct_value = ''.join(stop_profit_pct_df)
        initial_cash_df = df[df['paraName'] == 'initial_cash']['paraValue'].values
        initial_cash_value = ''.join(initial_cash_df)
        
        pb.param(name='backtest_symbol', value=backtest_symbol_value)
        pb.param(name='backtest_start_date', value=backtest_start_date_value)
        pb.param(name='backtest_end_date', value=backtest_end_date_df_value)
        pb.param(name='percent', value=percent_value)
        pb.param(name='stop_loss_pct', value=stop_loss_pct_value)
        pb.param(name='stop_profit_pct_df', value=stop_profit_pct_value)
        pb.param(name='initial_cash', value=initial_cash_value)
        
        print('全局变量 backtest_symbol', pb.param(name='backtest_symbol'))
        print('全局变量 backtest_start_date', pb.param(name='backtest_start_date'))
        print('全局变量 backtest_end_date', pb.param(name='backtest_end_date'))
        print('全局变量 percent', pb.param(name='percent'))
        print('全局变量 stop_loss_pct', pb.param(name='stop_loss_pct'))
        print('全局变量 stop_profit_pct_df', pb.param(name='stop_profit_pct_df'))
        print('全局变量 initial_cash', pb.param(name='initial_cash'))
    except Exception as error:
        print('获取公共参数错误：', error)
    else:
        print('获取公共参数完成')