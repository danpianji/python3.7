#-*- coding=utf-8 -*-
print("hello")
print("你好，世界")

#行和缩进
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    # 没有严格缩进，在执行时会报错
    print ("False")
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print (days)

#Python 引号
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。\
包含了多个语句"""
print (word);print (sentence);print (paragraph);

#python 中多行注释使用三个单引号(''')或三个双引号(""")。
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

#等待用户输入
raw_input("\n\nPress the enter key to exit.")


x2 = 'runoob'
print (x2)

#同一行显示多条语句
import sys; x='runoob2';sys.stdout.writelines(x)
print ('********************************')
#Print 输出
x='a'
y='b'
print (x)
print (y)
#Print 不换行输出
print (x, y)
print ('---------')
# 不换行输出
print (x,)
print (y)
print ('---------')