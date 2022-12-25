class Phone:
    IMEI = None
    producer = "ITcast"

    def call_by_4G(self):
        print("4G通话")

# 复写父类成员
class myPhone(Phone):
    producer = "HM"         # 复写父类成员属性

    def call_by_4G(self):   # 复写父类成员方法
        print("4G增强 通话")
        # 方式1
        print(f"父类厂商{Phone.producer}")
        print("父类方法",end='')
        Phone.call_by_4G(self)

        # 方式1
        print(f"父类厂商{super().producer}")
        print("父类方法",end='')
        super().call_by_4G()

phone = myPhone()
print(phone.producer)
phone.call_by_4G()

# 调用父类同名成员（子类中复写）
# 方式1
# 父类名.成员变量
# 父类名.成员方法(self)

# 方式2
# super()成员变量
# super()成员方法()