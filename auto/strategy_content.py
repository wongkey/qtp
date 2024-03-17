# -*- coding: utf-8 -*-
"""
策略内容函数
"""

import pybroker as pb
from pybroker import ExecContext

def buy_low(ctx):
    # If shares were already purchased and are currently being held, then return.
    if ctx.long_pos():
        return
    # If the latest close price is less than the previous day's low price,
    # then place a buy order.
    if ctx.bars >= 2 and ctx.close[-1] < ctx.low[-2]:
        # Buy a number of shares that is equal to 25% the portfolio.
        ctx.buy_shares = ctx.calc_target_shares(0.25)
        # Set the limit price of the order.
        ctx.buy_limit_price = ctx.close[-1] - 0.01
        # Hold the position for 3 bars before liquidating (in this case, 3 days).
        ctx.hold_bars = 3
        
def buy_with_indicator(ctx:ExecContext):
    #取得当前持仓状态
    pos = ctx.long_pos()
    percent = float(pb.param(name='percent'))
    
    if ctx.macd[-1] > 0 and ctx.macdsignal[-1] > 0:
        #如果未持仓
        if not pos: 
            # 将买单的限价设置为比最后收盘价低 0.01 的价格。
            #ctx.buy_limit_price = ctx.close[-1] - 0.01
            ctx.buy_limit_price = ctx.close[-1]
            # 买入1000股
            # ctx.buy_shares = 1000
            ctx.buy_shares = ctx.calc_target_shares(percent)
            #持有仓位5天
            ctx.hold_bars = 10
        #如果持仓
        else:
            ctx.buy_limit_price = ctx.close[-1]
            # 计算目标股票数量，根据 "percent" 参数确定应购买的股票数量
            ctx.buy_shares = ctx.calc_target_shares(percent)
            
            ctx.hold_bars = 10
    
    if ctx.macd[-1] < 0 and ctx.macdsignal[-1] < 0:
        #卖出全部股票
        ctx.sell_all_shares()
        #卖出100股
        #ctx.buy_shares = ctx.calc_target_shares(percent)
        #ctx.sell_shares = 1000
        # 设置止盈点位，根据 "stop_profit_pct" 参数确定止盈点位
        ctx.stop_profit_pct = pb.param(name='stop_profit_pct')
