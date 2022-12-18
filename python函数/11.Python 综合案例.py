money = 5000000
name = None
name = input("请输入姓名：")
def query():
    print("----------查询余额--------")
    print(f"{name}，你好，你的余额：{money}元")
def saving(num):
    global money
    money += num
    print("-----------存款-----------")
    print(f"{name}，你好，你存款{num}元成功")
def get_money(num):
    global money
    money -= num
    print("-----------取款-----------")
    print(f"{name}，你好，你取款{num}元成功")
def main():
    print(f"{name}，您好，欢迎来到黑吗银行ATM。请选择操作：")
    print("----------菜单------------")
    print("--------查询[1]-----------")
    print("--------存款[2]-----------")
    print("--------取款[3]-----------")
    print("--------返回[4]-----------")
    return input("请输入您的选择：")
while True:
    keyboard_input = main()
    if keyboard_input == '1':
        query()
        continue
    elif keyboard_input == '2':
        num = int(input("您想要存款多少钱？>>"))
        get_money(num)
        continue
    elif keyboard_input == '3':
        num = int(input("您想要取款多少钱？>>"))
        saving(num)
        continue
    else:
        print("退出程序")
        break