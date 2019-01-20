# -*- coding: UTF-8 -*-
import time
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
from queue import Queue

#定义收发队列
task_queue = Queue()
result_queue = Queue()

def get_task():
    return task_queue

def get_result():
    return result_queue

#创建类似的QueueManager
class QueueManager(BaseManager):
    pass

def win_run():
    # 第一步：使用QueueManager注册用于获取Queue的方法名称
    QueueManager.register("get_task_queue", callable=get_task)
    QueueManager.register("get_task_result", callable=get_result)

    # 第二步：连接到服务器
    m = QueueManager(address=("127.0.0.1", 8001), authkey=b"mima")
    #第三步：启动
    m.start()
    #第四步：获取queue对象
    try:
        task = m.get_task_queue()
        result = m.get_task_result()
        #添加任务
        for url in ["ImageUrl_"+str(i) for i in range(10)]:
            print ("put task %s ...." % url)
            task.put(url)
        print ("try get result....")
        for i in range(10):
            print ("result is %s" % result.get(timeout=10))
    except:
        print ("manager error")
    finally:
        m.shutdown()#一定要关闭，否则会报管道未关闭的错误

if __name__ == "__main__":#主函数
    freeze_support()#win下多进程可能会有问题，加这句可以缓解
    win_run()