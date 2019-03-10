# _*_ coding:utf-8 _*_
__author__ = 'Sheldon'
__date__ = '2019/2/21 20:29'
import socket
from datetime import datetime
from concurrent import futures
from multiprocessing import Pool
import os


def blocking_way():
    sock = socket.socket()
    # blocking
    sock.connect(('example.com', 80))
    request = 'GET / HTTP/1.0\r\nHOST: example.com\r\n\r\n'
    sock.send(request.encode('utf-8'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)
    print(f"Time:{datetime.now()} Threading:{os.getpid()} completed.")
    return response


def sync_way():
    res = []
    spent_time = []
    for i in range(10):
        t = datetime.now()
        res.append(blocking_way())
        spent_time.append(datetime.now() - t)
    print([i.microseconds for i in spent_time])
    return len(res)


def process_now():
    workers = 4
    with futures.ProcessPoolExecutor(workers) as executor:
        futs = [executor.submit(blocking_way) for i in range(10)]
    return len([fut.result() for fut in futs])

def process_mult():
    with Pool(processes=4) as pool:
        tasks = [pool.Process(target=blocking_way) for i in range(10)]
        return [task.start() for task in tasks]

if __name__ == '__main__':
    #sync_way()
    start = datetime.now()
    print(process_now())
    print(f"spent about {datetime.now() - start} s")
    print('------Multiprocessing------')
    start = datetime.now()
    print(f"{process_now()}spent about {datetime.now() - start} s")

