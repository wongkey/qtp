from pyecharts.charts import Bar
from pyecharts import options as opts

v1 = [23,13,44,63]
str = ["衬衫","衬衫","衬衫","衬衫"]
bar = (
       Bar()
       .add_xaxis(str)
       .add_yaxis('销售量', v1)
       .set_global_opts(title_opts=opts.TitleOpts(title='K线图',subtitle='分数'))
)
# bar = Bar("我的第一个图表","这里是副标题")
# bar.add("服装",["衬衫","衬衫","衬衫","衬衫","衬衫","衬衫"],[12,32,4,34,2,12])
# bar.show_config()

bar.render()
# bar.render("kline.html")