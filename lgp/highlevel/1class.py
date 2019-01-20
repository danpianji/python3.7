# -*- coding: UTF-8 -*-
print "你好"

"""
1、类： 
class ClassName:
   '类的帮助信息'   #类文档字符串
   class_suite  #类体

    def __init__(self):
        构造函数体
    def __del__(self):
        析构函数体
   
2、python对象销毁(垃圾回收):
del obj

例子：
a = 40      # 创建对象  <40>
b = a       # 增加引用， <40> 的计数
c = [b]     # 增加引用.  <40> 的计数

del a       # 减少引用 <40> 的计数
b = 100     # 减少引用 <40> 的计数
c[0] = -1   # 减少引用 <40> 的计数

Python 使用了引用计数这一简单技术来跟踪和回收垃圾
在 Python 内部记录着所有使用中的对象各有多少引用。
一个内部跟踪变量，称为一个引用计数器。
当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时， 
也就是说， 这个对象的引用计数变为0 时， 它被垃圾回收。但是回收不是"立即"的， 
由解释器在适当的时机，将垃圾对象占用的内存空间回收。

3、类的继承
继承语法 class 派生类名（基类名）：//... 基类名写在括号里，基本类是在类定义的时候，在元组之中指明的。

在python中继承中的一些特点：

    1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
    2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别在于类中调用普通函数时并不需要带上self参数
    3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。
    （先在本类中查找调用的方法，找不到才去基类中找）。
    
    基础重载方法

下表列出了一些通用的功能，你可以在自己的类重写：
序号	方法, 描述 & 简单的调用
1	__init__ ( self [,args...] ) 构造函数
简单的调用方法: obj = className(args)
2	__del__( self ) 析构方法, 删除一个对象
简单的调用方法 : del obj
3	__repr__( self ) 转化为供解释器读取的形式
简单的调用方法 : repr(obj)
4	__str__( self ) 用于将值转化为适于人阅读的形式
简单的调用方法 : str(obj)
5	__cmp__ ( self, x ) 对象比较
简单的调用方法 : cmp(obj, x)

"""


class Employee:
    '所有员工的基类'
    empCount = 0

    #构造函数
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    #析构函数
    def __del__(self):
        print "员工：", self.name,"被删除"

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

# 显示函数，输出Employee打印信息
def myShowFun():
    print "Employee.__doc__:", Employee.__doc__
    print "Employee.__name__:", Employee.__name__
    print "Employee.__module__:", Employee.__module__
    print "Employee.__bases__:", Employee.__bases__
    print "Employee.__dict__:", Employee.__dict__
    emp = Employee("lgp", 1000)
    emp.displayCount()
    emp.displayEmployee()
    try:
        if not hasattr(emp, "age"):
            setattr(emp, "age", 15)
        agenum = getattr(emp, "age")
        print agenum
        delattr(emp, "age")
        getattr(emp, "age")#异常代码
    except AttributeError:
        print "对象没有属性"
    except:
        print "exception failed"
    else:
        print "success"
    finally:
        del emp

#调用函数
myShowFun()


#self代表类的实例，而非类
class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()

#类继承例子
class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print "调用父类构造函数"

    def parentMethod(self):
        print '调用父类方法'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性 :", Parent.parentAttr

    def myMethod(self):
        print '调用父类方法'


class Child(Parent):  # 定义子类
    def __init__(self):
        print "调用子类构造方法"

    def childMethod(self):
        print '调用子类方法'

    def myMethod(self):
        print '调用子类方法重写方法'


c = Child()  # 实例化子类
c.childMethod()  # 调用子类的方法
c.parentMethod()  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法 - 设置属性值
c.getAttr()  # 再次调用父类的方法 - 获取属性值
c.myMethod() #调用子类重写的方法
del c

#运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print v1 + v2

"""
单下划线、双下划线、头尾双下划线说明：

    __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。

    _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *

    __foo: 双下划线的表示的是私有类型(private)的变量或方法, 只能是允许这个类本身进行访问了。

"""

class A:
   def foo(self):
      print('called A.foo()')
class B(A):
   def foo(self):
      print('called B.foo()')
   pass
class C(A):
   def foo(self):
      print('called C.foo()')
class D(B,C):#按顺序调用
   pass

if __name__ == '__main__':
   d = D()
   d.foo()