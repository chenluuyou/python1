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
- 封装
- 继承
- 多态

## 6.1封装
- 封装就是对对象的成员进行访问限制
- 封装的三个级别
    - Public
    - Protected
    - Private
    - Public,Protected,Private不是关键字
- 判别对象的位置
    - 对象内部
    - 对象外部
    - 子类中
[python中下划线的使用](https://blog.csdn.net/tcx1992/article/details/80105645)
- 私有
    - 私有成员是最高级别的封装，只能在当前类或对象中访问
    - 在成员前添加两个下划线即可
    
            class Person():
                # name是共有的成员
                name = "lulu"
                # __age是私有成员
                __age = 22
                
            p =Person()
            # name是公有变量
            print(p.name)
            # __age是私有变量
            print(p.__age) #会报错
    - Python的私有不是真私有，是一种成为name mangling的改名策略
    - 可以使用obj._classname__attribute
    
            print(p._Person__age)
- 受保护的封装 protected
    - 受保护的封装是将对象成员进行一定级别的封装，然后在类中或者在子类中都可以进行访问，但是在外部不可以
    - 封装方法：在成员名称前添加一个下划线即可
- 公开的 public
    - 公共的封装实际对成员没有任何操作，任何地方也可以访问
    
## 3.2 继承
- 继承就是一个类可以获得另外一个类中的成员属性和成员方法
- 作用：减少代码，增加代码的服用功能，同时可以设置类与类直接的关系
- 继承与被继承的概念
    - 被继承的类叫父类，也叫基类、超类
    - 用于继承的类叫子类，也叫派生类
    - 继承与被继承一定存在一个 is a 关系型
    
            # 在python中任何类都有一个共同的父类Object
            class Person():
                name = "NoName"
                age = 0
                def sleep(self):
                    print("Sleeping.....")
            # 父类写在括号里        
            class Teacher(Person): 
                pass
                
            t = Teacher()
            print(t.name)
            print(Teacher.name)
    - 继承的特征
        - 所有的类都继承自Object类，即所有的类都是Object的子类
        - 子类一旦继承父类，则可以使用父类中除私有成员外的所有内容
        - 子类继承父类后并没有将父类成员完全赋值到子类中，而是通过引用关系访问调用 见03.py
        - 子类中可以定义独有的成员的属性和方法           
        - 子类中定义的成员和父类中的成员如果相同，则优先使用子类成员
        - 子类如果想扩充父类的方法，则可以定义新方法的同时访问父类成员来进行代码重用
        可以使用父类名.父类成员来调用父类成员，也可以使用super().父类成员的格式来调用