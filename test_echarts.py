from typing import List, Sequence, Union

from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Kline, Line, Bar, Grid

# 数据
echarts_data = [
    ["2016-12-20", 17.99, 17.79, 17.7, 17.99, 29.00, 1, 0.02, -0.05, -0.05],
    ["2016-12-21", 17.83, 17.81, 17.77, 17.98, 30.00, 0, 0.00, -0.05, -0.06],
    ["2016-12-22", 17.85, 17.72, 17.65, 17.85, 21.00, 0, -0.03, -0.07, -0.06],
    ["2016-12-23", 17.77, 17.6, 17.54, 17.77, 18.00, 0, -0.04, -0.08, -0.05],
    ["2016-12-26", 17.56, 17.75, 17.39, 17.77, 16.00, 0, -0.04, -0.07, -0.05],
    ["2016-12-27", 17.73, 17.71, 17.65, 17.82, 10.00, 0, -0.06, -0.07, -0.04],
    ["2016-12-28", 17.72, 17.62, 17.49, 17.77, 26.00, 0, -0.09, -0.07, -0.03],
    ["2016-12-29", 17.6, 17.49, 17.43, 17.62, 28.00, 0, -0.09, -0.06, -0.02],
    ["2016-12-30", 17.53, 17.6, 17.47, 17.61, 22.00, 0, -0.05, -0.03, -0.01],
    ["2017-01-03", 17.6, 17.92, 17.57, 17.98, 28.00, 1, 0.00, 0.00, 0.00],
]

def split_data(origin_data) -> dict:
    datas = []
    times = []
    vols = []
    macds = []
    difs = []
    deas = []

    for i in range(len(origin_data)):
        datas.append(origin_data[i][1:])
        times.append(origin_data[i][0:1][0])
        vols.append(origin_data[i][5])
        macds.append(origin_data[i][7])
        difs.append(origin_data[i][8])
        deas.append(origin_data[i][9])
    vols = [int(v) for v in vols]

    return {
        "datas": datas,
        "times": times,
        "vols": vols,
        "macds": macds,
        "difs": difs,
        "deas": deas,
    }


def split_data_part() -> Sequence:
    mark_line_data = []
    idx = 0
    tag = 0
    vols = 0
    for i in range(len(data["times"])):
        if data["datas"][i][5] != 0 and tag == 0:
            idx = i
            vols = data["datas"][i][4]
            tag = 1
        if tag == 1:
            vols += data["datas"][i][4]
        if data["datas"][i][5] != 0 or tag == 1:
            mark_line_data.append(
                [
                    {
                        "xAxis": idx,
                        "yAxis": float("%.2f" % data["datas"][idx][3])
                        if data["datas"][idx][1] > data["datas"][idx][0]
                        else float("%.2f" % data["datas"][idx][2]),
                        "value": vols,
                    },
                    {
                        "xAxis": i,
                        "yAxis": float("%.2f" % data["datas"][i][3])
                        if data["datas"][i][1] > data["datas"][i][0]
                        else float("%.2f" % data["datas"][i][2]),
                    },
                ]
            )
            idx = i
            vols = data["datas"][i][4]
            tag = 2
        if tag == 2:
            vols += data["datas"][i][4]
        if data["datas"][i][5] != 0 and tag == 2:
            mark_line_data.append(
                [
                    {
                        "xAxis": idx,
                        "yAxis": float("%.2f" % data["datas"][idx][3])
                        if data["datas"][i][1] > data["datas"][i][0]
                        else float("%.2f" % data["datas"][i][2]),
                        "value": str(float("%.2f" % (vols / (i - idx + 1)))) + " M",
                    },
                    {
                        "xAxis": i,
                        "yAxis": float("%.2f" % data["datas"][i][3])
                        if data["datas"][i][1] > data["datas"][i][0]
                        else float("%.2f" % data["datas"][i][2]),
                    },
                ]
            )
            idx = i
            vols = data["datas"][i][4]
    return mark_line_data


def calculate_ma(day_count: int):
    result: List[Union[float, str]] = []

    for i in range(len(data["times"])):
        if i < day_count:
            result.append("-")
            continue
        sum_total = 0.0
        for j in range(day_count):
            sum_total += float(data["datas"][i - j][1])
        result.append(abs(float("%.2f" % (sum_total / day_count))))
    return result


def draw_chart():
    kline = (
        Kline()
        .add_xaxis(xaxis_data=data["times"])
        .add_yaxis(
            series_name="",
            y_axis=data["datas"],
            itemstyle_opts=opts.ItemStyleOpts(
                color="#ef232a",
                color0="#14b143",
                border_color="#ef232a",
                border_color0="#14b143",
            ),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                label_opts=opts.LabelOpts(
                    position="middle", color="blue", font_size=15
                ),
                data=split_data_part(),
                symbol=["circle", "none"],
            ),
        )
        .set_series_opts(
            markarea_opts=opts.MarkAreaOpts(is_silent=True, data=split_data_part())
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="K线周期图表", pos_left="0"),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                is_scale=True,
                boundary_gap=False,
                axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),
                split_number=20,
                min_="dataMin",
                max_="dataMax",
            ),
            yaxis_opts=opts.AxisOpts(
                is_scale=True, splitline_opts=opts.SplitLineOpts(is_show=True)
            ),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="line"),
            datazoom_opts=[
                opts.DataZoomOpts(
                    is_show=False, type_="inside", xaxis_index=[0, 0], range_end=100
                ),
                opts.DataZoomOpts(
                    is_show=True, xaxis_index=[0, 1], pos_top="97%", range_end=100
                ),
                opts.DataZoomOpts(is_show=False, xaxis_index=[0, 2], range_end=100),
            ],
            # 三个图的 axis 连在一块
            # axispointer_opts=opts.AxisPointerOpts(
            #     is_show=True,
            #     link=[{"xAxisIndex": "all"}],
            #     label=opts.LabelOpts(background_color="#777"),
            # ),
        )
    )

    kline_line = (
        Line()
        .add_xaxis(xaxis_data=data["times"])
        .add_yaxis(
            series_name="MA5",
            y_axis=calculate_ma(day_count=5),
            is_smooth=True,
            linestyle_opts=opts.LineStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="category",
                grid_index=1,
                axislabel_opts=opts.LabelOpts(is_show=False),
            ),
            yaxis_opts=opts.AxisOpts(
                grid_index=1,
                split_number=3,
                axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                axistick_opts=opts.AxisTickOpts(is_show=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(is_show=True),
            ),
        )
    )
    # Overlap Kline + Line
    overlap_kline_line = kline.overlap(kline_line)

    # Bar-1
    bar_1 = (
        Bar()
        .add_xaxis(xaxis_data=data["times"])
        .add_yaxis(
            series_name="Volumn",
            y_axis=data["vols"],
            xaxis_index=1,
            yaxis_index=1,
            label_opts=opts.LabelOpts(is_show=False),
            # 根据 echarts demo 的原版是这么写的
            # itemstyle_opts=opts.ItemStyleOpts(
            #     color=JsCode("""
            #     function(params) {
            #         var colorList;
            #         if (data.datas[params.dataIndex][1]>data.datas[params.dataIndex][0]) {
            #           colorList = '#ef232a';
            #         } else {
            #           colorList = '#14b143';
            #         }
            #         return colorList;
            #     }
            #     """)
            # )
            # 改进后在 grid 中 add_js_funcs 后变成如下
            itemstyle_opts=opts.ItemStyleOpts(
                color=JsCode(
                    """
                function(params) {
                    var colorList;
                    if (barData[params.dataIndex][1] > barData[params.dataIndex][0]) {
                        colorList = '#ef232a';
                    } else {
                        colorList = '#14b143';
                    }
                    return colorList;
                }
                """
                )
            ),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="category",
                grid_index=1,
                axislabel_opts=opts.LabelOpts(is_show=False),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )

    # Bar-2 (Overlap Bar + Line)
    bar_2 = (
        Bar()
        .add_xaxis(xaxis_data=data["times"])
        .add_yaxis(
            series_name="MACD",
            y_axis=data["macds"],
            xaxis_index=2,
            yaxis_index=2,
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(
                color=JsCode(
                    """
                        function(params) {
                            var colorList;
                            if (params.data >= 0) {
                              colorList = '#ef232a';
                            } else {
                              colorList = '#14b143';
                            }
                            return colorList;
                        }
                        """
                )
            ),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="category",
                grid_index=2,
                axislabel_opts=opts.LabelOpts(is_show=False),
            ),
            yaxis_opts=opts.AxisOpts(
                grid_index=2,
                split_number=4,
                axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                axistick_opts=opts.AxisTickOpts(is_show=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(is_show=True),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )

    line_2 = (
        Line()
        .add_xaxis(xaxis_data=data["times"])
        .add_yaxis(
            series_name="DIF",
            y_axis=data["difs"],
            xaxis_index=2,
            yaxis_index=2,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="DIF",
            y_axis=data["deas"],
            xaxis_index=2,
            yaxis_index=2,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(legend_opts=opts.LegendOpts(is_show=False))
    )
    # 最下面的柱状图和折线图
    overlap_bar_line = bar_2.overlap(line_2)

    # 最后的 Grid
    grid_chart = Grid()

    # 这个是为了把 data.datas 这个数据写入到 html 中,还没想到怎么跨 series 传值
    # demo 中的代码也是用全局变量传的
    grid_chart.add_js_funcs("var barData = {}".format(data["datas"]))

    # K线图和 MA5 的折线图
    grid_chart.add(
        overlap_kline_line,
        grid_opts=opts.GridOpts(pos_left="3%", pos_right="1%", height="60%"),
    )
    # Volumn 柱状图
    grid_chart.add(
        bar_1,
        grid_opts=opts.GridOpts(
            pos_left="3%", pos_right="1%", pos_top="71%", height="10%"
        ),
    )
    # MACD DIFS DEAS
    grid_chart.add(
        overlap_bar_line,
        grid_opts=opts.GridOpts(
            pos_left="3%", pos_right="1%", pos_top="82%", height="14%"
        ),
    )
    grid_chart.render("professional_kline_chart.html")


if __name__ == "__main__":
    data = split_data(origin_data=echarts_data)
    draw_chart()