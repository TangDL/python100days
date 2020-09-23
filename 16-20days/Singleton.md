# 单例模式

## 1.何为单例模式--Singleton
在文件的规模比较大时，使用全局变量进行参数的传递会导致参数混乱，有可能在多个文件中定义了多个同名的全局变量，混淆某个
全局变量在文件中都做了哪些操作。  
单例模式保证了在程序的不同位置都可以且仅可以取到同一个对象实例：如果实例不存在，会创建一个实例；
如果已存在就会返回这个实例。因为单例是一个类，所以你也可以为其提供相应的操作方法，以便于对这个实例进行管理。  
举个例子来说，比如你开发一款游戏软件，游戏中需要有“场景管理器”这样一种东西，用来管理游戏场景的切换、资源载入、
网络连接等等任务。这个管理器需要有多种方法和属性，在代码中很多地方会被调用，且被调用的必须是同一个管理器，否则既容易产生冲突，
也会浪费资源。这种情况下，单例模式就是一个很好的实现方法。

以下介绍4中实现单例模式的方法：
   - 使用函数装饰器实现单例
   - 使用类装饰器实现单例
   - 使用__new__方法实现单例
   - 使用meteclass实现单例
   
## 2.使用函数装饰器实现单例
~~~
import functools
def Singleton(cls):
    _instance = {}                             # 使用_instance 为dict很巧妙，其key时不可变类型，指向的地址不会被改变
    functools.wraps(cls)
    def wrapper():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return wrapper()

@Singleton
def ClassA():
    def __init__(self):
        pass

class1 = ClassA
class2 = ClassA

print(id(class1) == id(class2))          # 使用id关键字可以获得目标在python中的存储位置
~~~
使用不可变的类地址作为键，其实例作为值，每次创造实例时，首先查看该类是否存在实例，
存在的话直接返回该实例即可，否则新建一个实例并存放在字典中。

## 2.使用类装饰器实现单例
~~~
import functools
class Singleton(object):
    def __init__(self, cls):
        self._instance = {}
        self.cls = cls
    def __call__(self, *args, **kwargs):    #如果类实现了这个方法，相当于把这个类型的对象当作函数来使用，相当于 重载了括号运算符
        if self.cls not in self._instance:
            self._instance[self.cls] = self.cls()
        return self._instance[self.cls]

@Singleton
class ClassA(object):
    def __init__(self):
        pass

class1 = ClassA
class2 = ClassA

print(id(class1) == id(class2))    
~~~     
而且，和用函数装饰器定义的单例不同的是，由于类是面向对象的，因此可以如下创建单例：
~~~
class Cls3(object):
    pass
cls4 = Cls3()
cls5 = Cls3()

print(id(cls4) == id(cls5))
~~~

## 4.利用__new__关键字创建单例
在接着说另外两种方法之前，需要了解在 Python 中一个类和一个实例是通过哪些方法以怎样的顺序被创造的。

简单来说，元类(metaclass) 可以通过方法 __metaclass__ 创造了类(class)，而类(class)通过方法 __new__ 创造了实例(instance)。

在单例模式应用中，在创造类的过程中或者创造实例的过程中稍加控制达到最后产生的实例都是一个对象的目的。

使用 __new__ 方法在创造实例时进行干预，达到实现单例模式的目的。
~~~
import functools
class Singleton(object):
    _instance = None                   # 应当定义为全局变量，在__init__中初始话，因为None为不可变类型，因此在其他方法中无法修改，或调用
    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
           cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class1 = Singleton()
class2 = Singleton()

print(id(class1) == id(class2))
~~~

## 5.利用meteclass实现单例
和利用__new__方法类似，也是在实现类之前进行干预，从而到达实现单例的目的
首先简单了解一下type关键字创建类的方法：
- 使用type()函数时，如果只传入一个参数object，那么将返回该object的类型；
- 如果分别传入name，bases，dict这三个参数，那么type()函数将会创建一个对象；
- 使用class定义对象的时候，Python解释器调用type()函数来动态创建对象。
~~~
def func(self):
    print('gg')

ClassA = type('ClassA', (), {'func':func})

clsA = ClassA()    # 在创建claA时，由于对象本身会作为一个参数传入到类的方法中，因此func()函数必须有一个参数用来接受对象本身
clsA.func()
~~~

~~~
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Cls4(metaclass=Singleton):
    pass

cls1 = Cls4()
cls2 = Cls4()
print(id(cls1) == id(cls2))
~~~