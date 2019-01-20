#!/user/bin/env python
#coding:utf-8

import random
print random.random()           #输入0-1之间的随机数
print random.uniform(10,20)     #输出10-20之间的随机数
print random.randint(10,20)     #输出10-20之间的随机整数
print random.choice([x for x in range(1,100)]) #输出1-99间的随机数



class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print 'nNum = %d' % self.nNum

if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print 'The num = %d' % nNum
        inst.inc()

# 类的属性
class Static:
    StaticVar = 5
    def varfunc(self):
        print "self:",self.StaticVar
        print Static.StaticVar#打印属性
        self.StaticVar += 1
        print self.StaticVar

print Static.StaticVar
a = Static()
for i in range(3):
    a.varfunc()
print Static.StaticVar