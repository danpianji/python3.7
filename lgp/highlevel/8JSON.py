# -*- coding: UTF-8 -*-
import json
print "你好"


"""
json.dumps 	将 Python 对象编码成 JSON 字符串
json.loads	将已编码的 JSON 字符串解码为 Python 对象

python 原始类型向 json 类型的转化对照表：
Python 	JSON
dict 	object
list, tuple 	array
str, unicode 	string
int, long, float 	number
True 	true
False 	false
None 	null


json 类型转换到 python 的类型对照表：
JSON 	Python
object 	dict
array 	list
string 	unicode
number (int) 	int, long
number (real) 	float
true 	True
false 	False
null 	None
"""

jsonobj =  { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }
strJson = json.dumps(jsonobj)#obj转str
print strJson

#使用参数让 JSON 数据格式化输出：
print json.dumps(jsonobj, sort_keys=True, indent=4, separators=(',', ': '))

#loads str转json
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
text = json.loads(jsonData)
print text




