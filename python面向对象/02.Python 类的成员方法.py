class Student:
    # 成员属性
    name = None
    age = None
    # 成员方法
    def print_info(self):
        print(f"姓名{self.name}，年龄{self.age}")
    def say_hi(self,msg):
        print(f"大家好，我是{self.name}，{msg}")

stu1 = Student()
stu1.name = 'xfk'
stu1.age = 27
stu1.print_info()
stu1.say_hi("哎呦不错哦！")