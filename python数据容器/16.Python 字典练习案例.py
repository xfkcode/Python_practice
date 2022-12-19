# 1级员工加薪
info_dict ={
    "王力宏":{
        "部门":"科技部",
        "工资":7000,
        "级别":1,
    },
    "周杰伦":{
        "部门":"市场部",
        "工资":5000,
        "级别":2,
    },
    "林俊杰":{
        "部门":"市场部",
        "工资":7000,
        "级别":3,
    },
    "张学友":{
        "部门":"科技部",
        "工资":4000,
        "级别":1,
    },
    "刘德华":{
        "部门":"市场部",
        "工资":6000,
        "级别":2,
    },
}
print(f"升值加薪前{info_dict}")
# 遍历
for name in info_dict:
    if info_dict[name]["级别"] == 1:
        employee = info_dict[name]
        employee["级别"] = 2
        employee["工资"] += 1000
        info_dict[name] = employee
print(f"升值加薪后{info_dict}")