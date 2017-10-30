# -*-coding:gbk
import asyncio,threading

@asyncio.coroutine
def hello():
    print("hello world! (%s)" % threading.currentThread())
    r = yield from asyncio.sleep(1)
    print("Hello again! (%s)" % threading.currentThread())

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host,80)
    reader, writer = yield from connect
    print(reader,writer)
    header = 'GET / HTTP/1.0\r\nHOST: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host,line.decode('utf-8').rstrip()))
    writer.close()
    
loop = asyncio.get_event_loop()
task1 = [wget(host) for host in ['www.sina.com.cn','www.sohu.com','www.163.com']]
tasks = [hello(),hello(),task1]
loop.run_until_complete(asyncio.wait(task1))
loop.close()
