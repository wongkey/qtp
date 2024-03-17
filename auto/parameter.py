from sqlalchemy import text
from sqlalchemy import create_engine

import pandas as pd
import pybroker as pb
import datetime
import configparser

def get_init_parameters():
    try:
        print('开始取公共参数')

        # 创建ConfigParser对象
        config = configparser.ConfigParser()

        #配置文件路径：
        path = "auto/config.ini"

        #创建ConfigParser模块
        config = configparser.ConfigParser()

        #读取文件
        config.read(path, encoding="utf-8")

        #获取所有的section
        #sections = config.sections()
        #print(sections)

        # 获取配置项的值
        hostname = config.get('mysqldb', 'hostname')
        dbname = config.get('mysqldb', 'dbname')
        username = config.get('mysqldb', 'username')
        password = config.get('mysqldb', 'password')

        backtest_symbol = config.get('pybroker', 'backtest_symbol')
        backtest_start_date = config.get('pybroker', 'backtest_start_date')
        backtest_end_date = config.get('pybroker', 'backtest_end_date')
        initial_cash = config.get('pybroker', 'initial_cash')
        percent = config.get('pybroker', 'percent')
        stop_loss_pct = config.get('pybroker', 'stop_loss_pct')
        stop_profit_pct = config.get('pybroker', 'stop_profit_pct')

        tushare_token = config.get('tushare', 'tushare_token')
        last_update_data_date = config.get('tushare', 'last_update_data_date')

        print('hostname:',hostname)
        print('dbname:',dbname)
        print('username:',username)
        print('password:',password)
        
        print('backtest_symbol:',backtest_symbol)
        print('backtest_start_date:',backtest_start_date)
        print('backtest_end_date:',backtest_end_date)
        print('initial_cash:',initial_cash)
        print('percent:',percent)
        print('stop_loss_pct:',stop_loss_pct)
        print('stop_profit_pct:',stop_profit_pct)

        print('tushare_token:',tushare_token)
        print('last_update_data_date:',last_update_data_date)
 
        # 定义全局变量
        pb.param(name='hostname', value=hostname)
        pb.param(name='dbname', value=dbname)
        pb.param(name='username', value=username)
        pb.param(name='password', value=password)
        
        pb.param(name='backtest_symbol', value=backtest_symbol)
        pb.param(name='backtest_start_date', value=backtest_start_date)
        pb.param(name='backtest_end_date', value=backtest_end_date)
        pb.param(name='initial_cash', value=initial_cash)
        pb.param(name='percent', value=percent)
        pb.param(name='stop_loss_pct', value=stop_loss_pct)
        pb.param(name='stop_profit_pct', value=stop_profit_pct)

        pb.param(name='tushare_token', value=tushare_token)        
        pb.param(name='last_update_data_date', value=last_update_data_date)
        
        print('全局变量 hostname：', pb.param(name='hostname'))
        print('全局变量 dbname：', pb.param(name='dbname'))
        print('全局变量 username：', pb.param(name='username'))
        print('全局变量 password：', pb.param(name='password'))
        
        print('全局变量 backtest_symbol：', pb.param(name='backtest_symbol'))
        print('全局变量 backtest_start_date：', pb.param(name='backtest_start_date'))
        print('全局变量 backtest_end_date：', pb.param(name='backtest_end_date'))
        print('全局变量 initial_cash：', pb.param(name='initial_cash'))
        print('全局变量 percent：', pb.param(name='percent'))
        print('全局变量 stop_loss_pct：', pb.param(name='stop_loss_pct'))
        print('全局变量 stop_profit_pct：', pb.param(name='stop_profit_pct'))
        
        print('全局变量 tushare_token：', pb.param(name='tushare_token'))
        print('全局变量 last_update_data_date：', pb.param(name='last_update_data_date'))
        
    except Exception as error:
        print('获取公共参数错误：', error)
    else:
        print('获取公共参数完成')

def edit_last_update_data_date(engine):
    try:
        # 创建ConfigParser对象
        config = configparser.ConfigParser()

        #配置文件路径：
        path = "auto/config.ini"

        #创建ConfigParser模块
        config = configparser.ConfigParser()

        #读取文件
        config.read(path, encoding="utf-8")
        
        current_date = datetime.date.today()
        formatted_date = current_date.strftime("%Y%m%d")
        pb.param(name='last_update_data_date', value=formatted_date)
        
        print('更新数据截至日期')
        # 更新配置项的值
        config.set('tushare', 'last_update_data_date', formatted_date)

        # 写入到配置文件
        with open(path, 'w') as configfile:
            config.write(configfile)
        
    except Exception as error:
        print('更新数据截至日期错误：', error)
    else:
        print('更新数据截至日期完成')

def database() -> create_engine:
    try:
        hostname = pb.param(name='hostname')
        dbname = pb.param(name='dbname')
        username = pb.param(name='username')
        password =  pb.param(name='password')
        
        engine = create_engine('mysql+pymysql://' + username + ':' + password + '@' + hostname + '/' + dbname + '')
        
        return engine
    except Exception as error:
        print('创建数据库连接失败：', error)

def new_func():
    print('创建数据库连接成功')

'''改写数据库中最后更新日期 已作废
def last_update_data_date(engine):
    try:
        print('更新数据截至日期')
        conn = engine.connect()
        conn.execute("UPDATE parameter SET paraValue='' WHERE paraName='last_update_data_date'")
        conn.commit()
    except Exception as error:
        print('更新数据截至日期错误：', error)
    else:
        print('更新数据截至日期完成')
'''

'''从数据库中取得公共参数 已作废
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
'''