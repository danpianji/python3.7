# -*- coding: UTF-8 -*-
import time
from multiprocessing.managers import BaseManager


#创建QueueManager
class QueueManager(BaseManager):
    pass


#第一步：使用QueueManager注册用于获取Queue的方法名称
QueueManager.register("get_task_queue")
QueueManager.register("get_task_result")
#第二步：连接到服务器
m = QueueManager(address=("127.0.0.1", 8001), authkey=b"mima")
m.connect()#连接网络
#第三步：从网络获取Queue对象
task = m.get_task_queue()
result = m.get_task_result()
#第四步：从task队列获取任务，并把结果写入result队列
while not task.empty():
    image_url = task.get(True, timeout=5)
    print ("run task download ------->%s" % image_url)
    time.sleep(1)
    result.put("%s----------->success" % image_url)

#结束
print ("worker exit.........")