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
