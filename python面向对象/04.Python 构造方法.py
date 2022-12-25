# __init__()构造方法
class Stu:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("构造方法")

stu = Stu('xfk',27)
print(f"姓名{stu.name}，年龄{stu.age}")