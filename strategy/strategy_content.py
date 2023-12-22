# -*- coding: utf-8 -*-
"""
策略内容函数
"""

import pybroker as pb
from pybroker import ExecContext
        
def buy_with_indicator(ctx:ExecContext):
    #取得当前持仓状态
    pos = ctx.long_pos()
    
    if ctx.macd[-1] > 0 and ctx.macdsignal[-1] > 0:
        #如果未持仓
        if not pos: 
            # 将买单的限价设置为比最后收盘价低 0.01 的价格。
            ctx.buy_limit_price = ctx.close[-1] - 0.01
            # 买入100股
            ctx.buy_shares = 100
            #持有仓位5天
            ctx.hold_bars = 5
        #如果持仓
        else:
            # 计算目标股票数量，根据 "percent" 参数确定应购买的股票数量
            ctx.buy_shares = ctx.calc_target_shares(pb.param(name='percent'))
    
    if ctx.macd[-1] < 0 and ctx.macdsignal[-1] < 0:
        #卖出全部股票
        ctx.sell_all_shares()
        #卖出100股
        ctx.sell_shares = 100
        # 设置止盈点位，根据 "stop_profit_pct" 参数确定止盈点位
        ctx.stop_profit_pct = pb.param(name='stop_profit_pct')

