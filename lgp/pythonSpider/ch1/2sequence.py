# -*- coding: UTF-8 -*-

#序列化操作
try:
    import cPickle as pickle
except:
    import pickle

dict = {"name":"lgp", "age":20, "sex":'M'}
str = pickle.dumps(dict)
print str

dict2 = pickle.loads(str)
print dict2

#也可以将序列化的字符串写入文件存储