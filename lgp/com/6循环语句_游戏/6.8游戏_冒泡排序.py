# -*- coding: UTF-8 -*-

# 冒泡排序# 定义列表 list
arays = [1,8,2,6,3,9,4]
for i in range(len(arays)):
    for j in range(i+1):
        if arays[i] < arays[j]:
            # 实现连个变量的互换
            arays[i],arays[j] = arays[j],arays[i]
print arays