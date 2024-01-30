from sqlalchemy import text

def clear_data(engine):
    try:
        print('开始清除数据')
        
        conn = engine.connect()
        
        sql0 = text("DELETE FROM basic_data_stock_code")
        conn.execute(sql0)
        print('清除 basic_data_stock_code 数据完成')
        
        sql1 = text("DELETE FROM basic_data_stock_history")
        conn.execute(sql1)
        print('清除 basic_data_stock_history 数据完成')
        
        sql2 = text("DELETE FROM return_metrics")
        conn.execute(sql2)
        print('清除 return_metrics 数据完成')
        
        sql3 = text("DELETE FROM return_order")
        conn.execute(sql3)
        print('清除 return_order 数据完成')
        
        sql4 = text("DELETE FROM return_portfolio")
        conn.execute(sql4)
        print('清除 return_portfolio 数据完成')
        
        sql5 = text("DELETE FROM return_positions")
        conn.execute(sql5)
        print('清除 return_positions 数据完成')
        
        sql6 = text("DELETE FROM return_trades")
        conn.execute(sql6)
        print('清除 return_trades 数据完成')
        
        sql7 = text("DELETE FROM return_trades_df")
        conn.execute(sql7)
        print('清除 return_trades_df 数据完成')
        
        conn.commit()
    except Exception as error:
        print('清除数据错误：', error)
    else:
        print('清除数据完成')