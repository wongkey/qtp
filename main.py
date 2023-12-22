# -*- coding: utf-8 -*-
"""
主程序
"""

from strategy.strategy_execute import create_strategy

import datetime

def main():
    current_date = datetime.datetime.now()
    
    print("开始日期时间：", current_date)
    create_strategy()
    print("结束日期时间：", current_date)

if __name__ == '__main__':
    main()