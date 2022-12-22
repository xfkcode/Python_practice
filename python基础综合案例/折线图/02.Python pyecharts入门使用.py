from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
# 创建折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(["中国","美国","英国"])
# 添加y轴数据
line.add_yaxis("GDP",[30,20,10])
# 全局配置 set_global_opts()
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
# 通过render方法，将代码生成为图像
line.render()