# -*- coding: UTF-8 -*-
print "hehe "
#使用with代替try...finally f.close。
with open("test", "w") as fileReader:
    fileReader.write("hello world")

#读取文件
with open("test", "r") as fileReader:
    for str in fileReader.readlines():
        print str.strip()
