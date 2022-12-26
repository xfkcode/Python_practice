# 多态
# 多种状态，即完成某个行为时，使用不同的对象会得到不同的状态
# 同样的行为（函数），传入不同的运行对象，得到不同的状态

# 函数（方法）形参声明接收父类对象
# 实际传入父类的子类对象进行工作

class Animal:
    def speck(self):
        pass

class Dog(Animal):
    def speck(self):
        print("汪汪汪")
class Cat(Animal):
    def speck(self):
        print("喵喵喵")

def make_noise(animal: Animal):
    animal.speck()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)

# 抽象类（接口)
class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing(self):
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")
    def hot_wind(self):
        print("美的空调制热")
    def swing(self):
        print("美的空调左右摆风")

class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")
    def hot_wind(self):
        print("格力空调制热")
    def swing(self):
        print("格力空调左右摆风")

def make_cool(ac:AC):
    ac.cool_wind()

midea_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)