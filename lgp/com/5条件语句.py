# -*- coding: UTF-8 -*-
print "你好"
'''
Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false
 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现
 如果判断需要多个条件需同时判断时，
 可以使用 or （或），表示两个条件有一个成立时判断条件成功；
 使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
'''

# 例1：if 基本用法

flag = False
name = 'luren'
if name == 'python':  # 判断变量否为'python'
    flag = True  # 条件成立时设置标志为真
    print 'welcome boss'  # 并输出欢迎信息
else:
    print name  # 条件不成立时输出变量名称

# 例2：elif用法

num = 5
if num == 3:  # 判断num的值
    print 'boss'
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:  # 值小于零时输出
    print 'error'
else:
    print 'roadman'  # 条件均不成立时输出

num = 9
if num >= 0 and num <= 10:  # 判断值是否在0~10之间
    print 'hello'
# 输出结果: hello

num = 10
if num < 0 or num > 10:  # 判断值是否在小于0或大于10
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine

# 简单的语句组
# 你也可以在同一行的位置上使用if条件判断语句，如下实例：
var = 100
if (var == 100):print "变量 var 的值为100"
print "Good bye!"

# 一个简单的条件循环语句实现汉诺塔问题
def my_print(args):
    print args

def move(n, a, b, c):
    my_print ((a, '-->', c)) if n==1 else (move(n-1,a,c,b) or move(1,a,b,c) or move(n-1,b,a,c))

move (3, 'a', 'b', 'c')


"""


    汉诺塔问题描述

汉诺塔：汉诺塔（又称河内塔）问题是源于印度一个古老传说的益智玩具。大梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序摞着64片黄金圆盘。大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘。

    1、用递归解决问题，一个关键点是要有递归结束的条件
    2、当只有一个盘子的时候，直接就是A->C，这也是递归结束的条件
    3、当有两个盘子的时候，我们知道需要这样移动，A->B, A->C, B->C。
    4、当有三个或三个以上的盘子的时候，我们这样来考虑把最下面的盘子当做一块，其他盘子当做一块，那么，就简化成了上一步。A柱子是源，B柱子是当做临时转换用的源，C是目的
    需要注意的是，当经过上一步后，除了最下面的盘子其他的已经到了B柱子上了，这个时候，A柱子就是当做临时转换用的了，B柱子是源，C是目的。所以当n不等于1的时候，会回调两次函数，第一次参数的顺序是n,a,c,b。第二次是n,b,a,c

    c语言代码实现汉诺塔问题

void move(int n, char a, char b, char c)
{
   if(n==1)
   {
        printf("%c-->%c\n", a,c);
   }
   else
   {//要移动第n块盘子，需要建立在n-1块的基础上
        move(n-1, a, c, b);//a移动到b
        printf("%c-->%c\n", a, c);
        move(n-1, b, a, c);//上面的最后一段话
   }
}
"""


#python代码实现汉诺塔问题

def move(n, a, b, c):
    if(n==1):
        print(a+"-->"+c)
    else:
        move(n-1, a, c, b)
        print(a+"-->"+c)
        move(n-1, b, a, c)
move(3, 'a', 'b', 'c')