# -*- coding:gbk
from multiprocessing import Process,Queue
import os,time,random

#д���ݽ���ִ�еĴ���
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

#�����ݽ���ִ�еĴ��룺
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' %value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target = write, args=(q,))
    pr = Process(target = read, args=(q,))
    #�����ӽ���pw��д��
    pw.start()
    #�����ӽ���pr����ȡ
    pr.start()
    #�ȴ�pw����
    pw.join()
    #pr ��������ѭ�����޷��ȴ��������ֻ��ǿ����ֹ
    pr.terminate()
