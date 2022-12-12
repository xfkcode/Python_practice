name = "传智播客"
stock = 19.99
stock_code = "003032"
factor = 1.2
growth_days = 7
price = stock * factor ** growth_days
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock}")
print("每日增长系数：%.1f，经过%d天的增长后：股价到达了：%.2f"%(factor,growth_days,price))