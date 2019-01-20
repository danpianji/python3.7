# -*- coding: UTF-8 -*-
print ("hello")

import sys
sys.stdout.write("标准输出")

#读取键盘输入
# raw_input
# input
#input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回
"""
啥时候用raw_input()啥时候用input()?
字符的时候可以用raw_input()，当然不怕麻烦也可以用input()手动加''
int类型的时候最好用input()
2.7版本 raw_input 接收字符串
input 接收数字

3.0以后版本 只有input函数，没有raw_input函数了。
input 接收字符串和数字
"""

# str = raw_input("请输入：")
# print "你输入的内容是: ", str
#
# str2 = input("请输入：")
# print "你输入的内容是: ", str2

"""
打开和关闭文件 
open 函数
你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
语法：
file object = open(file_name [, access_mode][, buffering])
各个参数的细节如下：
file_name：
    file_name变量是一个包含了你要访问的文件名称的字符串值。
access_mode：
    access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。
    这个参数是非强制的，默认文件访问模式为只读(r)。
buffering:
    如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。
    如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认
    
    File对象的属性

一个文件被打开后，你有一个file对象，你可以得到有关该文件的各种信息。

以下是和file对象相关的所有属性的列表：
属性	描述
file.closed	返回true如果文件已被关闭，否则返回false。
file.mode	返回被打开文件的访问模式。
file.name	返回文件的名称。
file.softspace	如果用print输出后，必须跟一个空格符，则返回false。否则返回true。
"""

# 打开一个文件,并写入文件.使用with代替try..finally
#with open("name","w") as f
#f.write("content")
fo = open("0Test.txt", "w")
fo.write( "www.runoob.com!\nVery good site!\n")
fo.close()
print ("文件名: ", fo.name)
print ("是否已关闭 : ", fo.closed)
print ("访问模式 : ", fo.mode)
print ("末尾是否强制加空格 : ", fo.softspace)

# 打开一个文件,并读取文件内容
fo = open("0Test.txt", "r")
str = fo.read(10)
print (str)
# 查找当前位置
position = fo.tell()
print ("当前文件位置 : ", position)
# 把指针再次重新定位到文件开头
fo.seek(0)
print ("position",position)
str = fo.read(10)
print ("重新读取字符串 : ", str)
fo.close()

#按行读取文件内容
fo = open("0Test.txt", "r")
while 1:
    str = fo.readline()
    if len(str)>0:
        print (str)
    else:
        break#退出循环
fo.close()#关闭文件

"""
重命名和删除文件

Python的os模块提供了帮你执行文件处理操作的方法，比如重命名和删除文件。

要使用这个模块，你必须先导入它，然后才可以调用相关的各种功能。
rename()方法：
rename()方法需要两个参数，当前的文件名和新文件名。

语法：
os.rename(current_file_name, new_file_name)
os.remove("test2.txt")
os.mkdir("newdir") 创建目录
rmdir()方法 执行方法前，目录中不能存在文件
chdir()方法  os.chdir("/home/newdir")
os.getcwd() 获得当前目录
"""

import os

#创建测试文件test1.txt
f = open("test1.txt", "w")
f.close()
# 重命名文件test1.txt到test2.txt。
#os.path.exists(pathname)可以判断文件和文件夹是否存在。但不能区分是否是文件所以 判断文件用isfile(filename)
if os.path.isfile("test2.txt"):
    os.remove("test2.txt")
os.rename("test1.txt", "test2.txt")
print (os.getcwd())


# 打开文件
fo = open("test.txt", "w")
print ("文件名为: ", fo.name)
seq = ["菜鸟教程 1\n", "菜鸟教程 2"]
fo.writelines( seq )

# 关闭文件
fo.close()



