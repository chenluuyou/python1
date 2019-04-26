# 0 OOP-Python面向对象
- python面向对象
- 面向对象编程
    - 基础
    - 公有私有
    - 继承
    - 组合，Mixin
- 魔法函数
    - 魔法函数概述
    - 构造魔法函数
    - 运算类魔法函数

# 1.面向对象概述(ObjectOriented,OO)
- OOP思想
    - 接触到一个任务，首先想到的是任务这个世界的构成，是由模型构成的
- 几个名词
    - OO：面向对象
    - OOA：面向对象分析
    - OOD：面向对象的设计
    - OOI：面向对象的实现
    - OOP:面向对象的编程
    - OOA->OOD->OOI：面向对象的实现过程
- 类和对象的概念
    - 类：抽象名词，代表一个集合，共性的事物
    - 对象：巨象的事物，单个个体
    - 类和对象的关系
        - 一个具象，代表一类事物的某一个个体
        - 一个是抽象，代表一大类事物
    - 类中的内容具有两个内容：
        - 表明事物的特征，叫做属性（变量）
        - 表明事物功能或动作，叫做成员方法（函数）
        
# 2.类的基本实现
- 类的命名
    - 遵守变量命名的规范
    - 大驼峰（由一个或多个单词构成，每个单词首字母大写，单词和单词之间直接相连）
    - 尽量避开跟系统命名相似的命名
- 声明一个类
    - 必须用class关键字
    - 类由属性和方法构成，其他不许出现
    - 成员属性定义可以直接使用变量赋值，允许使用None
    - 案例 01.py
- 实例化类

            变量 = 类名()  实例化一个对象
- 访问对象成员
    - 使用点操作符
    
            obj.成员属性名称
            obj.成员方法
- 可以通过默认内置变量检查类和对象的所有成员
    - 对象所有成员的检查
    
            # dict前后各有两个下划线
            obj.__dict__
    - 类所有的成员
    
            #dict前后各有两个下划线
            class_name.__dict__
            
            
# 3.Anaconda基本使用
- Anaconda主要是一个虚拟环境管理器
- 还是一个安装包管理器
- conda list:显示Anaconda安装的包
- conda env list:显示Anaconda的虚拟环境列表
- conda create -n xxx python=3.7

# 4.类和对象的成员分析
- 类和对象都可以储存成员，成员可以归类所有，也可以归对象所有
- 类存储成员时使用的是与类关联的一个对象
- 对象存储成员是存储在当前对象中
- 对象访问一个成员时，如果对象中没有该成员，尝试访问类中的同名成员
    如果对象中有此成员，一定使用对象中的成员
    
        class A():
            name = "lulu"
            age = 18
            def say(self):
                self.name = "lulu"
                self.age = 20
        # 此时A称为类实例        
        print(A.name)
        print(A.age)
        print(id(A.name))
        print(id(A.age))
        print("*" * 20)
        a = A()
        
        print(a.name)
        print(a.age)
        print(id(a.name))
        print(id(a.age))
- 此案例说明类实例的属性和其对象的的实例的属性在不对对象的实例属性赋值的前提下指向同一变量

      class A():
            name = "lulu"
            age = 18
            def say(self):
                self.name = "lulu"
                self.age = 20
        # 此时A称为类实例        
        print(A.name)
        print(A.age)
        print(id(A.name))
        print(id(A.age))
        print("*" * 20)
        a = A()
        print(A.__dict__)
        print(a.__dict__)
        a.name = "angel"
        a.age = 22
        print(a.__dict__)
        
        print(a.name)
        print(a.age)
        print(id(a.name))
        print(id(a.age))
- 此案例说明若对对象的属性赋值的情况下，则对象实例和类实例的属性不指向同一变量
- 创建对象的时候，类中的成员不会放入对象之中，而是得到一个空对象没有成员
- 通过对象对类中成员重新赋值或通过对象添加成员时，对应成员会保存在对象中，而不会修改类成员

# 5.关于self

    class Student():
        name = "lulu"
        age = 18
        def say(self):
            self.name = "angel"
            self.age = 20
            print("My name is {0}".format(self.name))
            print("My age is {0}".format(self.age))
            
        def sayagain(s):
            self.name = "angel"
            self.age = 20
            print("My name is {0}".format(s.name))
            print("My age is {0}".format(s.age))
            
    yueyue = Student()
    yueyue.say()
    yueyue.sayagain()
- self在对象的方法中表示当前对象本身，如果通过对象调用一个方法，那么该对象会自动传入到当前方法的第一个参数中
- self并不是关键字，只是一个用于接受对象的普通参数，理论上可以用任何一个普通变量名代替
- 方法中有self形参的方法成为非绑定类方法，可以通过对象访问，没有self的是绑定类方法，只能通过类访问

        class Teacher():
            name = "dana"
            age = 30
            def say(self):
                self.name = "yaona"
                self.age = 28
                  print("My name is {0}".format(self.name))
                  print("My age is {0}".format(self.age))
            def sayagain():
            print("Hello,nice to see you again")
            
        t = Teacher()
        t.say()
        Teacher.sayagain()
- 使用类访问绑定类的方法时，如果类方法中需要访问当前类的成员时

        print(__class__.name)
        print(__class__.age)
- 这种访问类成员的方法也可以在对象的方法访问类的成员时使用
- 关于self的案例

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
        
# 6.面向对象的三大特性
                
        