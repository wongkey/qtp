    #strategy.add_execution(fn=buy_with_stop_loss, symbols=[pb.param(name='stock_code')])
    #strategy.add_execution(fn=buy_low, symbols=[pb.param(name='stock_code')])
    #strategy.add_execution(fn=buy_with_indicator, symbols=[pb.param(name='stock_code')])
    #cmma_20 = pb.indicator('cmma_20', cmma, lookback=20)
    #strategy.add_execution(buy_with_indicator, symbols=[pb.param(name='stock_code')], indicators=cmma_20)

    #i_macd_dif = pb.indicator('macd_dif', macd_dif, lookback=0)
    #i_macd_dea = pb.indicator('macd_dea', macd_dea, lookback=0)
    
    #indicator_set = IndicatorSet()
    #indicator_set.add(i_macd_dif, i_macd_dea)
    #indicator_set(df)

    #strategy.add_execution(buy_with_macd, symbols=[pb.param(name='stock_code')], indicators=get_data_macd())