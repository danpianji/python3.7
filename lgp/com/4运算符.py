# -*- coding: UTF-8 -*-
print "中文"
'''
Python语言支持以下类型的运算符:
    算术运算符
    比较（关系）运算符
    赋值运算符
    逻辑运算符
    位运算符
    成员运算符
    身份运算符
    运算符优先级
 '''

# Python算术运算符
print "\n\n# Python算术运算符 + - * / % ** //"
a = 21
b = 10
c = 0

c = a + b
print "1 - c = a + b 的值为：", c

c = a - b
print "2 - c = a - b 的值为：", c

c = a * b
print "3 - c = a * b 的值为：", c

c = a / b
print "4 - c = a / b 的值为：", c

c = a % b
print "5 - c = a % b 的值为：", c

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print "6 - c = a ** b 的值为：", c

a = 10
b = 5
c = a // b
print "7 - c = a // b 的值为：", c

# Python比较运算符
print "\n\n# Python比较运算符 == != <> > < >= <="
a = 21
b = 10
c = 0

if (a == b):
    print "1 - a 等于 b"
else:
    print "1 - a 不等于 b"

if (a != b):
    print "2 - a 不等于 b"
else:
    print "2 - a 等于 b"

if (a <> b):
    print "3 - a 不等于 b"
else:
    print "3 - a 等于 b"

if (a < b):
    print "4 - a 小于 b"
else:
    print "4 - a 大于等于 b"

if (a > b):
    print "5 - a 大于 b"
else:
    print "5 - a 小于等于 b"

# 修改变量 a 和 b 的值
a = 5
b = 20
if (a <= b):
    print "6 - a 小于等于 b"
else:
    print "6 - a 大于  b"

if (b >= a):
    print "7 - b 大于等于 a"
else:
    print "7 - b 小于 a"

# Python赋值运算符
print "\n\n# Python赋值运算符 = += -= *= /= %= **= 取幂数 //= 取整"
a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c += a
print "2 - c 的值为：", c

c *= a
print "3 - c 的值为：", c

c /= a
print "4 - c 的值为：", c

c = 2
c %= a
print "5 - c 的值为：", c

c **= a
print "6 - c 的值为：", c

c //= a
print "7 - c 的值为：", c

# Python位运算符 按位运算符是把数字看作二进制来进行计算的
print "\n\n# Python位运算符 & | ^异或 ~取反"
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b;  # 12 = 0000 1100
print "1 - c 的值为：", c

c = a | b;  # 61 = 0011 1101
print "2 - c 的值为：", c

c = a ^ b;  # 49 = 0011 0001
print "3 - c 的值为：", c

c = ~a;  # -61 = 1100 0011
print "4 - c 的值为：", c

c = a << 2;  # 240 = 1111 0000
print "5 - c 的值为：", c

c = a >> 2;  # 15 = 0000 1111
print "6 - c 的值为：", c

# Python逻辑运算符
print "\n\n# Python逻辑运算符 and  or  not"
a = 10
b = 20

if (a and b):
    print "1 - 变量 a 和 b 都为 true"
else:
    print "1 - 变量 a 和 b 有一个不为 true"

if (a or b):
    print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
    print "2 - 变量 a 和 b 都不为 true"

# 修改变量 a 的值
a = 0
if (a and b):
    print "3 - 变量 a 和 b 都为 true"
else:
    print "3 - 变量 a 和 b 有一个不为 true"

if (a or b):
    print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
    print "4 - 变量 a 和 b 都不为 true"

if not (a and b):
    print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
else:
    print "5 - 变量 a 和 b 都为 true"

# Python成员运算符 Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组
print "\n\n# Python成员运算符 in | not in "
a = 10
b = 20
list = [1, 2, 3, 4, 5];

if (a in list):
    print "1 - 变量 a 在给定的列表中 list 中"
else:
    print "1 - 变量 a 不在给定的列表中 list 中"

if (b not in list):
    print "2 - 变量 b 不在给定的列表中 list 中"
else:
    print "2 - 变量 b 在给定的列表中 list 中"

# 修改变量 a 的值
a = 2
if (a in list):
    print "3 - 变量 a 在给定的列表中 list 中"
else:
    print "3 - 变量 a 不在给定的列表中 list 中"

# Python身份运算符
# 身份运算符用于比较两个对象的存储单元
# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等
# 字符串和小整数 -5 ~ 256 is 比较相同因为使用的id相同
# ----经测试64位ide下整数,float,long都是具有相同id的
"""
事实上Python
为了优化速度，使用了小整数对象池，避免为整数频繁申请和销毁内存空间。而Python
对小整数的定义是[-5, 257)，只有数字在 - 5
到256之间它们的id才会相等，超过了这个范围就不行了，同样的道理，字符串对象也有一个类似的缓冲池，
超过区间范围内自然不会相等了
"""
print "\n\n# Python身份运算符 is | not is "
a = 20
b = 20
print "id(a)=",id(a)
print "id(b)=",id(b)
if (a is b):
    print "1 - a 和 b 有相同的标识"
else:
    print "1 - a 和 b 没有相同的标识"

if (a is not b):
    print "2 - a 和 b 没有相同的标识"
else:
    print "2 - a 和 b 有相同的标识"

# 修改变量 b 的值
b = 30
print "id(b)=",id(b)
if (a is b):
    print "3 - a 和 b 有相同的标识"
else:
    print "3 - a 和 b 没有相同的标识"

if (a is not b):
    print "4 - a 和 b 没有相同的标识"
else:
    print "4 - a 和 b 有相同的标识"

c=123456789L
d=123456789L
print "id(c)=",id(c),"  c=",c
print "id(d)=",id(d),"  d=",d
if ( c is d ):
    print "c is d 有相同的id标识"
else :
    print "c is d 没有相同的id标识"
