from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

#x, y = Faker.choose(), Faker.values()
x=['周一', '周二', '周三', '周四', '周五', '周六', '周日']
y=[88, 102, 47, 107, 130, 31, 58]

buy_points = {"周二": 0, "周三": 100}

print(x)
print(y)
print(buy_points)

c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(x)
    .add_yaxis(
        "商家A",
        y,
        # MarkPointOpts：标记点配置项
        markpoint_opts=opts.MarkPointOpts(
            # 标记点数据
            data=[
                *[
                # MarkPointItem：标记点数据项
                opts.MarkPointItem(
                     # 标注名称
                    name="自定义标记点", 
                    type_ = None,
                    value_index = None,
                    value_dim = None,
                    coord=[day,value], #这里是直角坐标系x轴第三个，y轴第三个
                    value=value,
                    x = None,  #一般默认就好
                    y = None,  #一般默认就好
                    symbol = None,  #一般默认就好
                    symbol_size = None,  #一般默认就好
                    itemstyle_opts = None,
                )
                for day, value in buy_points.items()
                ],
            ],
            
            symbol = None,  #一般默认就好
            symbol_size = None,  #一般默认就好
            label_opts = opts.LabelOpts(position="inside", color="#fff"),          
        ),
    )
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkPoint（自定义）"))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False)) #不显示标签
    .render("bar_markpoint_custom.html")
)
