# 闭包
## 1.何为闭包？
**在一个内部函数中，对外部作用域的变量进行引用（且外部函数的返回值往往为内部函数），则内部函数往往称之为闭包**
注意，引用的应当是外部作用域的变量，若引用的变量不在外部作用域中，会外部的环境不构成作用域，都不构成闭包
比如：
~~~
def A(x):
    def B(y):
        return x + y
    return B             # 注意是return B，不是B()，后者返回的是一个函数
~~~
函数B()就称之为一个闭包。

## 2.常见错误
### 2.1.闭包中无法对外部不可变的变量进行修改
比如：
~~~
def A(x):
    def B(x):
        x += 2
        print(x)
        return x
    print(x) 
    B(x) 
    print(x)
~~~
返回的结果为：
~~~
2
4
2
~~~
可见，当内部函数构成闭包的情况下，内部函数引用外部变量x，在内部作用域中可对x进行改变，
但是当x是不可变类型时，内部的改变将导致x指向另外一个地址，这就使得内部的x成功改变，但是外部的x指向的额还是原来的地址
当引用的外部变量是可变类型时，将在原来的地址上对x进行改变。即闭包无法改变外部函数局部变量指向的内存地址

### 2.2.for循环无法构成外部作用域
比如：
~~~
flist = []
for i in range(3):
    def plus2(i):                   # 这样写并没有引用外部变量，不构成闭包
        return 2*i
    flist.append(plus2(i))

for func in flist:
    print(func)
~~~
输出为：
~~~
0
2
4
~~~
~~~
flist = []
for i in range(3):
    def plusx(x):                   # 引用的外部变量i是会变化的，无法构成闭包
        return x*i
    flist.append(plusx)

for func in flist:
    print(func(2))
~~~
输出为：
~~~
4
4
4
~~~
原因在于，loop在python中并没有作用域的概念，flist在往里面添加plus的时候，并没有保存到i的值，而是当执行f(2)的时候才去取，
但是此时for循环已经结束，i=2，所以结果都是4
可修改为：
~~~
flist = []
for i in range(3):
    def middle(i):
        def plusx(x):                   # 引用的外部变量i被外部函数middle固定住，不再发生变化，形成闭包
            return x*i
        return plusx
    flist.append(middle(i))             # 往里面添加的函数相当于是x*0, x*1, x*2

for func in flist:
    print(func(2))
~~~

## 3.闭包的作用
**闭包可以保存当前的运行环境**。以一个类似棋盘游戏的例子来说明。假设棋盘大小为50*50，左上角为坐标系原点origin(0,0)，
需要一个函数，接收2个参数，分别为方向(direction)，步长(step)，该函数控制棋子的运动。 这里需要说明的是，
每次运动的起点都是上次运动结束的终点。

~~~~
origin = [0, 0]
def board(pos=origin):
    def move(dir, step):
        pos[0] += step * dir[0]
        pos[1] += step * dir[1]
        return pos
    return move

player = board()
print(player([0, 1], 10))
print(player([1, 0], 20))
print(player([-1, 0], 10))
~~~~
结果是：
~~~
[0, 10]
[20, 10]
[10, 10]
~~~
注意，在这里origin是list，为可变类型，上文中提到的x是int，为不可变类型，因为，在这个例子中，闭包中对外部变量
进行操作是可以影响到外部的origin的。

闭包在爬虫和web中有很广泛的应用（还没学到），并且闭包也是装饰器的基础。闭包最大的作用就是通过对当前运行环境的保存
，从而提高代码的可复用性。