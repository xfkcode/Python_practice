# Json数据格式1（Python字典）
{"anme":"admin","age":18}
# Json数据格式2（Python嵌套字典的列表）
[{"anme":"admin","age":18},{"anme":"xfk","age":18}]

# python数据和Json数据的相互转换
import json
data = [{"anme":"admin","age":18},{"anme":"xfk","age":18}]
json_str = json.dumps(data,ensure_ascii=False)   # python>>>json
print(f"json数据{json_str},\n类型{type(json_str)}")
s1 = '[{"anme":"admin","age":18},{"anme":"xfk","age":18}]'
data1 = json.loads(s1)                            # json>>>python
print(f"python数据{data1}，\n类型{type(data1)}")
s2 = '{"anme":"admin","age":18}'
data2 = json.loads(s2)
print(f"python数据{data2}，\n类型{type(data2)}")