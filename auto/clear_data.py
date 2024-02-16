from sqlalchemy import text

def clear_basic_data(engine):
    try:
        print('开始清除数据')
        
        conn = engine.connect()
        
        sql00 = text("DELETE FROM basic_data_stock_code_akshare")
        conn.execute(sql00)
        conn.commit()
        print('清除 basic_data_stock_code_akshare 数据完成')

        sql01 = text("DELETE FROM basic_data_stock_code_tushare")
        conn.execute(sql01)
        conn.commit()
        print('清除 basic_data_stock_code_tushare 数据完成')
        
        sql02 = text("DELETE FROM basic_trade_date_tushare")
        conn.execute(sql02)
        conn.commit()
        print('清除 basic_trade_date_tushare 数据完成')

        sql10 = text("DELETE FROM basic_stock_history_day_bfq_akshare")
        conn.execute(sql10)
        conn.commit()
        print('清除 basic_stock_history_day_bfq_akshare 数据完成')
        
        sql11 = text("DELETE FROM basic_stock_history_day_qfq_akshare")
        conn.execute(sql11)
        conn.commit()
        print('清除 basic_stock_history_day_qfq_akshare 数据完成')

        sql12 = text("DELETE FROM basic_stock_history_day_hfq_akshare")
        conn.execute(sql12)
        conn.commit()
        print('清除 basic_stock_history_day_hfq_akshare 数据完成')        
        
        sql13 = text("DELETE FROM basic_stock_history_day_bfq_tushare")
        conn.execute(sql13)
        conn.commit()
        print('清除 basic_stock_history_day_bfq_tushare 数据完成')

        sql14 = text("DELETE FROM basic_stock_history_day_qfq_tushare")
        conn.execute(sql14)
        conn.commit()
        print('清除 basic_stock_history_day_qfq_tushare 数据完成')

        sql15 = text("DELETE FROM basic_stock_history_day_hfq_tushare")
        conn.execute(sql15)
        conn.commit()
        print('清除 basic_stock_history_day_hfq_tushare 数据完成')
        
    except Exception as error:
        print('清除数据错误：', error)
    else:
        print('清除数据完成')
        
def clear_backtest_data(engine):
    try:
        print('开始清除回测数据')
        
        conn = engine.connect()

        sql00 = text("DELETE FROM return_metrics")
        conn.execute(sql00)
        conn.commit()
        print('清除 return_metrics 数据完成')
        
        sql01 = text("DELETE FROM return_order")
        conn.execute(sql01)
        conn.commit()
        print('清除 return_order 数据完成')
        
        sql02 = text("DELETE FROM return_portfolio")
        conn.execute(sql02)
        conn.commit()
        print('清除 return_portfolio 数据完成')
        
        sql03 = text("DELETE FROM return_positions")
        conn.execute(sql03)
        conn.commit()
        print('清除 return_positions 数据完成')
        
        sql04 = text("DELETE FROM return_trades")
        conn.execute(sql04)
        conn.commit()
        print('清除 return_trades 数据完成')
        
    except Exception as error:
        print('清除回测数据错误：', error)
    else:
        print('清除回测数据完成')