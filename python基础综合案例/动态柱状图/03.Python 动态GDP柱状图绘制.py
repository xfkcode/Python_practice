from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts,TitleOpts
from pyecharts.globals import ThemeType

f = open("./动态柱状图数据/1960-2019全球GDP数据.csv","r",encoding="GB2312")
data_lines = f.readlines()
f.close()
# 删除第一行
data_lines.pop(0)
# {年份：[[国家，GDP],[国家，GDP],...]，年份：[[国家，GDP],[国家，GDP],...],...}
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])      # 年份
    country =  line.split(",")[1]       # 国家
    gdp = float(line.split(",")[2])     # gdp数据
    try:
        data_dict[year].append([country,gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country,gdp])
# print(data_dict)

# 创建时间线对象
timeline = Timeline({"theme":ThemeType.LIGHT})
# 排序年份
sorted_year = sorted(data_dict.keys())
for year in sorted_year:
    data_dict[year].sort(key=lambda element: element[1],reverse=True)
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1])
    # 柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)",y_data,label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    timeline.add(bar,str(year))

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
timeline.render("1960-2019全球GDP前8国家.html")
