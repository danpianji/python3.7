# -*- coding: UTF-8 -*-
print "你好"
"""
1、循环语句2种，while循环和for循环
2、关键字 break continue pass
    2.1、pass是空语句，是为了保持程序结构的完整性
3、循环可以嵌套
注意：无限循环你可以使用 CTRL+C 来中断循环。
在 python 中，while … else 在循环条件为 false 时执行 else 语句块：
"""
#1、while循环
numbers = [12, 9, 8, 5, 4]
odd = []
even = []
while len(numbers) > 0 :
    number = numbers.pop()
    if(number%2==0):
        even.append(number)
    else:
        odd.append(number)
print "odd:",odd
print "even:",even

#2、while循环
count = 0
while (count < 9):
    print 'The count is:', count
    count = count + 1

print "Good bye!"

#while 语句时还有另外两个重要的命令 continue，break 来跳过循环，
# continue 用于跳过该次循环，break 则是用于退出循环，
# 此外"判断条件"还可以是个常值，表示循环必定成立，具体用法如下：
# continue 和 break 用法

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print i  # 输出双数2、4、6、8、10

i = 1
while 1:  # 循环条件为1必定成立
    print i  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break

#3 for 循环
for letter in 'Python':  # 第一个实例
    print '当前字母 :', letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print '当前水果 :', fruit

#通过序列索引迭代
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print '当前水果 :', fruits[index]
"""
   使用内置
   enumerate
   函数进行遍历:

   for index, item in enumerate(sequence):
       process(index, item)
"""
fruits = ['banana', 'apple',  'mango']
for index,item in enumerate(fruits):
   print '当前水果 :',index, item