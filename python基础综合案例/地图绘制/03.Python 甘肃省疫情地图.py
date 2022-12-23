import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts,VisualMapOpts

f = open("./地图数据/疫情.txt","r",encoding="UTF-8")
data = f.read()
f.close()

data_dict =json.loads(data)
cities_data = data_dict['areaTree'][0]['children'][20]['children']

data_list = []
for city_data in cities_data:
    city_name = city_data['name'] + '市'
    city_confirm = city_data['total']['confirm']
    data_list.append((city_name,city_confirm))
data_list.extend([('酒泉市',200),('嘉峪关市',1),('武威市',1000),('临夏回族自治州',5),('甘南藏族自治州',5)])
print(data_list)

map = Map()
map.add("甘肃省疫情分布",data_list,"甘肃")
map.set_global_opts(
    title_opts=TitleOpts("甘肃省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"label":"1-99人","color":"#CCFFFF"},
            {"min":100,"max":999,"label":"100-999人","color":"#FFFF99"},
            {"min":1000,"max":4999,"label":"1000-4999人","color":"#FF9966"},
            {"min":5000,"max":9999,"label":"5000-9999人","color":"#FF6666"},
            {"min":10000,"max":99999,"label":"10000-99999人","color":"#CC3333"},
            {"min":100000,"label":"100000+","color":"#990033"}
        ]
    )
)
map.render("甘肃省疫情地图.html")