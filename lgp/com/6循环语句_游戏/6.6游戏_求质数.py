# -*- coding: UTF-8 -*-
print "你好"
"""
1、质数：除了1和本身没有其他因子的数就是质数
"""
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'

# 输出 2 到 100 简的质数
prime = []
for num in range(2, 100):  # 迭代 2 到 100 之间的数字
   for i in range(2, num):  # 根据因子迭代
      if num % i == 0:  # 确定第一个因子
         break  # 跳出当前循环
   else:  # 循环的 else 部分
      prime.append(num)
print prime