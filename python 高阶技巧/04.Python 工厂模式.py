"""
工厂模式
"""
class Person:
    pass
class Worker(Person):
    pass
class Teacher(Person):
    pass
class Student(Person):
    pass

class PersonFactory:
    def get_person(self,p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 't':
            return Teacher()
        else:
            return Student()

pf = PersonFactory()
worker = pf.get_person('w')
student = pf.get_person('s')
teacher = pf.get_person('t')