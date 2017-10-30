# -*- coding:gbk

import time, threading,os
#新线程执行的代码
def loop():
    print('thread %s is running....' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    balance = balance + n
    balance = balance * n
    balance = balance / n
    balance = balance - n
#    print('balance of thread %s is %d' %(threading.current_thread().getName(),balance) )

def run_thread(n):
    for i in range(40000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
            
tlist = []
for i in range(1,50):
    t = threading.Thread(target=run_thread, args=(i,))
    tlist.append(t)
    t.start()

for t in tlist:
    t.join()
print(balance)
'''
print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
'''
