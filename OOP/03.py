# 在python中任何类都有一个共同的父类Object
class Person():
    name = "NoName"
    age = 0

    def sleep(self):
        print("Sleeping.....")


# 父类写在括号里
class Teacher(Person):
    def make_test(self):
        pass


t = Teacher()
print(t.name)
print(Teacher.name)
print(id(Teacher.name))
print(id(t.name))
print(id(Person.name))