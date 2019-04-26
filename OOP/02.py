class A():
    name = "lulu"
    age = 22

    def __init__(self):
        self.name = "haha"
        self.age = 18

    def say(self):
        print(self.name)
        print(self.age)


class B():
    name = "aaaa"
    age = 16


a = A()
a.say()
A.say(a)
A.say(A)
A.say(B)