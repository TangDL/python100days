#1.数据结构和算法
- 算法：解决问题的方法和步骤
- 评价算法的好坏：渐进时间复杂度和渐进空间复杂度
- 渐进时间复杂度的大O标记：   
        O(c)-常量时间复杂度：布隆过滤器/哈希存储   
        O(log2(n))-对数时间复杂度：折半查找（二分查找）   
        O(n)-线性时间复杂度：顺序查找/桶排序   
        O(n*log2(n))-对数线性时间复杂度：高级排序算法（归并排序，快速排序）   
        O(n<sup>2</sup>)-平方时间复杂度：简单排序算法（选择排序，插入排序，冒泡排序）
        O(n<sup>2</sup>)-立方时间复杂度：Floyd算法/矩阵乘法   
        O(2<sup>n</sup>)-指数时间复杂度：汉诺塔算法      
        O(n!)-阶乘时间复杂度：旅行经销商问题-NP
##1.1排序算法和查找算法
###1.1.1简单选择排序
````
def slect_sort(origin_item, comp=lambda x, y:x<y):
    items = origin_item[:]
    for i in range(len(items)-1):
        min_index = i
        for j in range(i+1, len(item)-1):
            if comp(items[j], item[i]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items
````

###1.1.2高质量冒泡排序
~~~
def bubble_sort(origin_items, comp=lambda x,y:x>y):
    items = origin_items
    for i in range(len(items)-1):
        swapped = False
        for j in range(i, len(items)-i-1):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items)-i-1, i, -1):
                if comp(items[j-1], items[j]):
                    items[j-1], items[j] = items[j], items[j-1]
        else:
            break
    return items
~~~

###1.1.3归并排序
~~~
def merge_sort(items, comp=lambda x,y:x<=y):
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)
def merge(items1, items2, comp):
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items
~~~

###1.1.4顺序查找
~~~
def seq_search(items, key):
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1
~~~

###1.1.5折半查找
~~~
def bin_search(items, key):
    start, end = 0, len(items) - 1
    mid = (start + end) // 2
    if key > items[mid]:
        start = mid + 1
    elif key < items[mid]:
        end = mid - 1
    else:
        return mid
    return -1
~~~

##1.2生成式（推导式）语法
- 使用生成式的优点：1.延迟计算，一次只返回一个结果，节省内存开销； 2.提高代码可读性
~~~
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票价格大于100元的股票构造一个新的字典
prices2 = {key:value for key, value in prices.item() if value>100}
~~~

##1.3嵌套列表
~~~
names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
scores = [[] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        score[row][col] = floate(input(f'请输入{name}的{course}的成绩:'))
        print(scores)
~~~

##1.4heapq,itertools的用法
###1.4.1heapq构建堆结构并进行相关操作
~~~
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nsmallest(3, list2, key=lambda x:x['price']))
print(heapq.nlargest(3, list1))
print(heapqpop(list1))        # 弹出堆中的最小元素
print(heapqpush(list1, 22))   # 将元素22压入list1中
print(heapify(list1))         # 将列表list1转换成堆
~~~

###1.4.2itertools迭代器的相关操作
- 一个关于可迭代对象的模块
~~~
import itertools

itertools.permutations('ABCD', 2)     # 生成长度为2的无序无重复的所有可能排列组合        
itertools.combinations('ABCDE', 3)    # 生成长度为3的有序无重复的所有可能排列组合 
itertools.product('ABCD', '123')      # 生成输入的笛卡尔积
~~~

##1.5collections 模块
- python内建的一个集合模块，提供许多有用的集合类
~~~
from collections import Counter, nametuple, deque, defaultdict, OrderedDict, ChainMap
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)                   # 找出列表中各元素的出现次数
print(counter.most_common(3))

Point = nametuple('Point', ['x', 'y'])     # 设定一种以tuple为基础的简单类

q = deque(list)
q.appendleft('')                           # 为list提供从头部开始添加和删除元素
q.popleft()

d = defaultdict(list)                      # 若a中不存在指定键，则创建该键，并以输入作为其键值

o = OrderDict()                            # 使得o中添加的元素以添加的先后次序进行排列

c = ChainMap(dict1, dict2, dict3)          # 将输入的dict链接成一个
~~~

## 1.6常用算法
- 穷举法：暴力破解法，列举出所有的可能结果，直到找到正确答案    
- 贪婪算法：在求解时，总是选择在当前看来最优的选择，不追求最优解，快速找到满意解    
- 分治法：把一个复杂的问题分解成两个或更多的相同或相似的子问题，再把子问题分解成更小的相似子问题，直到可以直接求解的程度，最后
将子问题的解进行合并得到原问题的解
- 回溯法：又成试探法，按照选优条件向前搜索，当搜索到某一步发现当前的选择并不优或者达不到目标时，就退回一步重新选择    
- 动态规划：基本思想是将问题分解成若干个子问题，先求解并保留这些子问题的解，避免产生大量的重复运算
 
 ###1.6.1穷举法--百钱白鸡问题和五人分鱼
 - **百钱白鸡问题**：公鸡5元一只 母鸡3元一只 小鸡1元三只，用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
~~~
for x  in range(20):
    for y in range(33):
        z = 100 - x - y
        if 5*x+3y+z//3 == 100 and z % 3 == 0:
            print(x, y, z)
~~~
- **五人分鱼问题**：A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己
的一份 B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
~~~
fish_num = 6
enough = True
while 1:
    for _ in range(5):
        if (fish_num - 1) % 5 == 0：
            fish_num = (fish_num - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        print(fish_num)
        break
    fish_num += 5
~~~

###1.6.2贪婪算法--小偷背包
**小偷背包**：假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。很显然，他不能把所有物品都装进背包，
所以必须确定拿走哪些物品，留下哪些物品。
名称	价格（美元）	重量（kg）
电脑	200	        20
收音机	20	        4
钟	    175	        10
花瓶	50	        2
书	    10	        1
油画	90	        9
/* 关键是通过性价比来进行求解，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解 */
参考代码：thief_backpage.py

###1.6.3分治算法--快速排序
**快速排序**：选择中枢轴对元素进行划分，左边的元素都比中枢轴小，右边的元素都比中枢轴大
时间复杂度：O(nlog(n))
空间复杂度：O(nlog(n))
参考代码：quick_sort.py

###1.6.3回溯算法--骑士巡逻
**骑士巡逻**：骑士走日，要求遍历棋盘中的每一个点而不重复
递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择，
比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。

###1.6.4动态规划--斐波那契数列和子列表元素之和的最大值
**动态规划**：适用于有重叠子问题和最优子结构性质的问题
使用动态规划方法所耗时间往往远少于朴素解法(用空间换取时间)

*子列表元素之和的最大值**:
子列表指的是列表中索引（下标）连续的元素构成的列表；列表中的元素是int类型，可能包含正整数、0、负整数；
程序输入列表中的元素，输出子列表元素求和的最大值

#2.函数的使用
- 函数的作用：
   1. 函数可以赋值给变量   
   2. 函数可以作为函数的参数
   3. 函数可以作为函数的返回值

- 函数的高阶用法--lambda,map,filter   
arr = list(map(lambda x:x**2, filter(lambda x:x%2, range(10))))  
filter：第一个参数是函数，输入变量x返回True或者False，若True则输入的x通过。 
arr = [x**2 for x in range(10) in x%2==0]

- 函数参数的类型：   
   - 位置参数
   - 可变参数
   - 关键字参数
   - 命名关键字参数
   
- 函数的元信息：给函数的参数进行注释，增加代码的可读性

- 匿名函数和内联函数的用法（lambda, filter）

- 闭包和作用域问题
   - 何为闭包？闭包常见错误？闭包的作用？
   - python搜索变量的LEGB顺序（Local->Embedded->Global->Build-in）
      - Local：函数内的名字空间
      -Embedded：外部嵌套函数的名字空间
      -Global：函数定义所在模块的名字空间
      -Build-in：python内置模块的名字空间
   - global和nonlocal的关键字作用：
      - global:声明和定义全局变量（要么直接使用现有的全局作用域的变量，要么定义一个变量放到全局作用域）。当需要在局部作用域
      中对外部变量进行修改时，需要对应用的变量使用global进行全局声明           
      - nonlocal:声明使用嵌套作用域的变量（嵌套作用域必须有该变量，否则报错）。即函数A中有函数B，若想在函数B中使用
      函数A的中变量，需要使用nonlocal关键字进行声明

- 装饰器函数（使用和取消装饰器）
   - 装饰器的定义
   - 三重嵌套，在装饰器中传入参数
   - functools.wraps的使用，将原函数的__name__赋值给wrapper
   
# 3.面向对象相关知识 

- 对象的复制（深复制/深拷⻉/深度克隆和浅复制/浅拷⻉/影⼦克隆）
   - 这三对关系说的其实是一样的都是在讲：深拷贝和浅拷贝
   - 复制：只是进行对象的引用，对象内存地址完全没有改变
   - 浅拷贝：改变了容器的内存地址，但是容器内部元素的内存地址完全没有改变
      - 使用方法：
         - copy.copy()
         - 切片操作[:]
         - 工厂函数，如list/dir/set
   - 深拷贝：完全拷贝了一个样本，容器和容器内部元素的内存地址都不一样
   - 非容器类型的对象，如原子类型的对象（数字，字符串），不存在拷贝
   - 如果元组变量只含有原子类型的变量，则不存在深拷贝，也就是说副本和原件的内存地址其实是一样的
- 魔法属性和方法
   - 魔法属性：
       - \_\_dict__:   是一个类最常用的属性之一了，它又分为类的__dict__属性和实例的__dict__属性
          - 类的__dict__属性存储了类定义的所有类属性、类方法等组成的键值对，但不包括继承而来的属性和方法
          - 实例的__dict__属性存储了所有的实例属性的键值对，如果没有就为空；__init__方法其实就是对__dict__属性的初始化赋值；
       - \_\_doc__:    该属性记录了类的说明文档，用类和实例引用指向的都是类的__doc__属性,如果没有默认为None。
       - \_\_module__: 该属性记录类定义的位置，如果定义的位置正好是主程序，那么该值为"\_\_main__",否则是类属于的模块的名字；
       - \_\_class__:  该属性指向该实例的类，即实例指向类对象，类对象指向元类；
       - \_\_slots__:  该属性起到限制动态绑定属性和方法的作用，该属性是一个元组，默认是不存在的，需要手动定义并且只对当前的类起作用，
                     只有添加到元组中的名字才能被动态添加属性，否则报错！
          - __slots__属性定义好后，限制了一个类的实例的属性以及可以动态添加的属性和方法；
          - __slots__属性定义好后，不得在类中定义元组中已有的同名的方法；
   - 魔法方法：
      - \_\_new__:    该方法是类创建实例调用的第一个方法，返回一个实例；这是一个实例从无到有必须调用的方法，
                       在单例模式中常用，其他不常用。
      - \_\_init__:   该方法可以说是类最常用的方法了，python在调用new方法后会紧接着调用init方法,
                      我们将实例的一些初始化操作放在该方法中，即对__dict__属性进行操作；
      - \_\_del__:    该方法在实例对象引用计数变为0或del关键字调用的时候触发执行。
      - \_\_repr__:   该方法在print调用或者repr调用时执行，用来定义类的描述信息，每个类都应该有这个方法
- 元类和元编程：
                对象是通过类创建的，类是通过元类创建的，元类提供了创建类的元信息。所有的类都直接或间接的继承自object，
                所有的元类都直接或间接的继承type，例如使用元类来实现单例模式。
                ~~~
                import threading
                
                class SingletonMeta(type):                    # 继承自type类
                    def __init__(cls, *args, **kwargs):
                        cls._instance = None
                        cls.lock = threading.Lock()
                        super(SingletonMeta, cls).__init__(*args, **kwargs)
                    def __call__(cls, *args, **kwargs):
                        if cls._instance is None:
                            with cls.lock:
                                if cls._instance is None:
                                    cls._instance = super().__call__(*args, **kwargs)
                        return cls._instance
                
                class President(metaclass=SingletonMeta):
                    def __init__(self):
                        pass
                
                p1 = President()
                p2 = President()
                
                print(id(p1) == id(p2))
                ~~~
- 面向对象设计原则：
   - 单一职责原则：
        ⼀个类只做该做的事情（类的设计要⾼内聚）
   - 开闭原则： 
        实体软件应该对扩展开放，对修改封闭。在程序需要进行拓展的时候，不能去修改原有的代码，
        实现一个热插拔的效果。简言之，是为了使程序的扩展性好，易于维护和升级。想要达到这样的效果，我们需要使用接口和抽象类；
   - 里氏替换原则：
        任何基类可以出现的地方，子类一定可以出现。LSP 是继承复用的基石，只有当派生类可以替换掉基类，且软件单位的功能不
        受到影响时，基类才能真正被复用，而派生类也能够在基类的基础上增加新的行为。里氏代换原则是对开闭原则的补充。实现
        开闭原则的关键步骤就是抽象化，而基类与子类的继承关系就是抽象化的具体实现，所以里氏代换原则是对实现抽象化的具体步骤的规范。
   - 接口隔离原则：
        使用多个隔离的接口，比使用单个接口要好。它还有另外一个意思是：降低类之间的耦合度；
   - 合成聚合复用原则：
        尽量使用合成/聚合的方式，而不是使用继承。
   - 迪米特法则： 
        不要给没有必然联系的对象发消息
        一个实体应当尽量少地与其他实体之间发生相互作用，使得系统功能模块相对独立。
   
- GOF设计模式
   - 创建型模式：单例、工厂、建造者、原型
   - 结构型模式：适配器、外观、代理
   - 行为模式  ：迭代器、观察者、策略、状态
   
- 生成器和迭代器
   - 如果设计一个迭代器类，如list，dict等，可以使用__iter__或者__next__方法
~~~
  
class Fib(object):
    """创建一个迭代器"""
    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.index = 0

    def __iter__(self):                                     # 使得iterator具有iterable的接口，这一块暂时还看不明白，
                                                            # 可迭代的对象有个 iter 方法，每次都实例化一个新的迭代器；
                                                            # 而迭代器要实现 next 方法，返回单个元素，此外还要实现 iter 方法，
                                                            # 返回迭代器本身。因此，迭代器是可迭代的，但是，可迭代对象不是迭代器。
        return self

    def __next__(self):
        if self.index < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.index += 1
            return self.a
        raise StopIteration()                              # 迭代结束，抛出异常
~~~
   - 生成器： 只要函数的定义体中有yield关键字，那么函数就是一个生成器。
              一个生成器也是一个迭代器，当一个生成器函数被调用时，返回一个生成器对象，当next方法被第一次调用时，生成器函数
              开始执行，直到yield语句，yield的值会在next方法调用时返回
              注意：类形式的生成器是可以重复使用的，而函数形式的生成器是不可以重复使用的（原因在于函数形式的生成器，没有实现
              __iter__方法）
~~~
 class Counter(object):
     def __init__(self, low, high):
         self.low = low
         self.high = high
     def __iter__(self):                        # 实现了iter方法，每次调用该迭代对象时，都会生成一个新的迭代器
          counter = self.low
         while self.high >= counter:
              yield counter
~~~

~~~
def counter_generator(low, high):
    while low <= high:
       yield low
       low += 1
~~~

# 4.线程、进程和异步处理
 - 线程：系统分配cpu的基本单位
 使用情况：
    - 程序需要维护许多共享的状态（尤其是可变状态），python中的list，set和dict都是线程安全的，所以使用多线程而不是多进程维护共享
    状态的代价相对较小
    - 程序需要花费大量的时间在IO操作上，并没有太多并行计算的要求并且不用占用太多内存
 使用方法：
    - thread.Thread(target, args).start
    - 多个线程竞争临界资源的时候，需要加锁对临界资源进行保护（with threading.Lock）
      多个线程竞争⼀个资源 - 保护临界资源 - 锁（Lock/RLock）
    - pool = ThreadPoolExecutor(max_workers=10)创建线程池
    - 多个线程竞争多个资源（线程数>资源数） - 信号量（Semaphore）
    - 多个线程的调度  - 暂停线程的执行/唤醒等待中的线程（Condition）
       lock = threading.Lock
       condiction = threading.Condition(lock)
    
 - 进程：系统分配内存的基本单位
 使用情况：
    - 程序需要执行计算密集型任务（如：字节码操作，数据处理，科学计算）
    - 程序的输入可以并行的分成块，并且可以将运算结果合并
    - 程序在内存使用方面并没有任何限制并且不强依赖于IO操作
 使用方法：主要是使用类Process，进程间共享数据可以使用管道，套接字等
 使用示例：
~~~
"""
import concurrent.futures
import math
PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5

def is_prime(n):
"""判断素数"""
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True
def main():
"""主函数"""
with concurrent.futures.ProcessPoolExecutor() as executor:            # 着的一段代码写的真实简洁优美
    for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
        print('%d is prime: %s' % (number, prime))
if __name__ == '__main__':
    main()
~~~

- 异步IO
  这一部分过于复杂，暂时pass
