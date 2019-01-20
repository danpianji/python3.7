# -*- coding: UTF-8 -*-

#1、例子
var = 1
var2 = 10
print var,var2

del var , var2
"""
1、
Python 支持四种不同的数值类型：

    整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。
    长整型(long integers) - 无限大小的整数，整数最后是一个大写或小写的L。
    浮点型(floating point real values) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
    复数(complex numbers) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。


2、Python Number 类型转换

int(x [,base ])         将x转换为一个整数  
long(x [,base ])        将x转换为一个长整数  
float(x )               将x转换到一个浮点数  
complex(real [,imag ])  创建一个复数  
str(x )                 将对象 x 转换为字符串  
repr(x )                将对象 x 转换为表达式字符串  
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象  
tuple(s )               将序列 s 转换为一个元组  
list(s )                将序列 s 转换为一个列表  
chr(x )                 将一个整数转换为一个字符  
unichr(x )              将一个整数转换为Unicode字符  
ord(x )                 将一个字符转换为它的整数值  
hex(x )                 将一个整数转换为一个十六进制字符串  
oct(x )                 将一个整数转换为一个八进制字符串  

3、Python数学函数
函数	返回值 ( 描述 )
abs(x)	返回数字的绝对值，如abs(-10) 返回 10
ceil(x) 	返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)	如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
exp(x) 	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x) 	返回数字的下舍整数，如math.floor(4.9)返回 4
log(x) 	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x) 	返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...) 	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...) 	返回给定参数的最小值，参数可以为序列。
modf(x) 	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	x**y 运算后的值。
round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x) 	返回数字x的平方根

4、Python随机数函数

随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。

Python包含以下常用随机数函数：
函数	描述
choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step]) 	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random() 	随机生成下一个实数，它在[0,1)范围内。
seed([x]) 	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst) 	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。

5、Python三角函数

Python包括以下三角函数：
函数	描述
acos(x)	返回x的反余弦弧度值。
asin(x)	返回x的反正弦弧度值。
atan(x)	返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	返回的x弧度的正弦值。
tan(x)	返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度

6、cmp(x, y) 函数在 python3.x 中不可用，可用以下函数替代：

operator.lt(a, b)           lt(a, b) 相当于 a < b
operator.le(a, b)           le(a,b) 相当于 a <= b
operator.eq(a, b)           eq(a,b) 相当于 a == b
operator.ne(a, b)           ne(a,b) 相当于 a != b
operator.ge(a, b)           gt(a,b) 相当于 a > b
operator.gt(a, b)           ge(a, b)相当于 a>= b

7、abs() 和 fabs() 区别

    1、abs()是一个内置函数，而fabs()在math模块中定义的。
    2、fabs()函数只适用于float和integer类型，而 abs() 也适用于复数。

"""