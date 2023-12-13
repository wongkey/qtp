import pybroker as pb
from pybroker import ExecContext


# 定义交易策略：如果当前没有持有该股票，则买入股票，并设置止盈点位
def buy_with_stop_loss(ctx: ExecContext):

    pos = ctx.long_pos()
    if not pos:
        # 计算目标股票数量，根据 "percent" 参数确定应购买的股票数量
        ctx.buy_shares = ctx.calc_target_shares(pb.param(name='percent'))
        ctx.hold_bars = 100
    else:
        ctx.sell_shares = pos.shares
        # 设置止盈点位，根据 "stop_profit_pct" 参数确定止盈点位
        ctx.stop_profit_pct = pb.param(name='stop_profit_pct')

'''
如果最后收盘价低于前一根K线的最低价，并且该股票没有未平仓的多头头寸，则购买该股票的股份。
将买单的限价设置为比最后收盘价低 0.01 的价格。
持有头寸 3 天后以市价平仓。
在 AAPL 和 MSFT 上执行这些规则，为每只股票分配最多 25% 的投资组合。
'''

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
        
def buy_with_indicator(ctx):   
    if ctx.long_pos():
        return
    # Place a buy order if the most recent value of the 20 day CMMA is < 0:
    if ctx.indicator('cmma_20')[-1] < 0:
        ctx.buy_shares = ctx.calc_target_shares(1)
        ctx.hold_bars = 3