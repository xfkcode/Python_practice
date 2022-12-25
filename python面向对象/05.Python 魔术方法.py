# 魔术方法
class Stu:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # 1.__str__()
    # 控制类转换为字符串的行为，对象地址（默认）
    def __str__(self):
        return f"Stu类对象，name={self.name}，age={self.age}"
    # 2.__lt__小于符号比较方法（小于和大于都可）
    def __lt__(self, other):
        return self.age < other.age
    # 3。__le__小于等于符号比较方法（小于等于和大于等都可）
    def __le__(self, other):
        return self.age <= other.age
    # 4.__eq__比较运算符，比较内存地址（默认）
    def __eq__(self, other):
        return self.age == other.age

stu1 = Stu('xfk',27)
stu2 = Stu('tq',22)
print(stu1)

print(stu1<stu2)
print(stu1>stu2)

print(stu1<=stu2)
print(stu1>=stu2)

stu3 = Stu('xfk',25)
stu4 = Stu('tq',25)
print(stu3==stu4)