# -*- coding:UTF-8 -*-
print "hello word"
"""
1、re.match与re.search的区别
re.match(pattern, string, flags=0)：re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
re.search(pattern, string, flags=0)：re.search 扫描整个字符串并返回第一个成功的匹配
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
而re.search匹配整个字符串，直到找到一个匹配。

2、检索和替换
Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。
语法：
re.sub(pattern, repl, string, count=0, flags=0)
参数：
    pattern : 正则中的模式字符串。
    repl : 替换的字符串，也可为一个函数。
    string : 要被查找替换的原始字符串。
    count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
    
3、re.compile 函数
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

语法格式为：
re.compile(pattern[, flags])

4、findall
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
findall(string[, pos[, endpos]])

5、re.finditer
和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
re.finditer(pattern, string, flags=0)

6、re.split
split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：
re.split(pattern, string[, maxsplit=0, flags=0])
"""


import re
###################################################################
#1、match
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配，用span()返回开始和结束位置的一个元组
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配因为返回none，所以不能调用span()函数返回一个元组。

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
    print "matchObj.groups : ", matchObj.groups()
else:
    print "No match!!"

#######################################################################################################
#2、替换
phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print "电话号码是: ", num

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print "电话号码是 : ", num

#repl 参数是一个函数 即sub中第二个参数
# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
#####################################################################################
"""
group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
span([group]) 方法返回 (start(group), end(group))
"""
#3、compile
pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字 生成一个正则表达式（ Pattern ）对象
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print m
m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print m
m = pattern.match('one12twothree34four', 3, 10) # 当匹配成功时返回一个 Match 对象
print m
print m.group()   # 可省略 0
print m.start()
print m.end()
print m.span()


pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
print m                               # 匹配成功，返回一个 Match 对象
print m.group(0)                            # 返回匹配成功的整个子串
print m.span(0)                             # 返回匹配成功的整个子串的索引
print m.group(1)                            # 返回第一个分组匹配成功的子串
print m.span(1)                             # 返回第一个分组匹配成功的子串的索引
print m.group(2)                            # 返回第二个分组匹配成功的子串
print m.span(2)                             # 返回第二个分组匹配成功的子串的索引
print m.groups()                            # 等价于 (m.group(1), m.group(2), ...)
##############################################################################################
#4、findall
# 查找字符串中的所有数字：
pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)

#################################################################################################
#5、finditer
#re.finditer(pattern, string, flags=0)
it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print (match.group() )
#################################################################################################
# 6、split
#re.split(pattern, string[, maxsplit=0, flags=0])
print re.split('\W+', 'runoob, runoob, runoob.')
print re.split('(\W+)', ' runoob, runoob, runoob.')
print re.split('\W+', ' runoob, runoob, runoob.', 1)
print re.split('a*', 'hello world')  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割