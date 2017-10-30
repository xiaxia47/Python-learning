#-*- coding:utf-8
import socket,time
#						IPV4     ,协议：UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999')

while True:
    data, addr = s.recvfrom(9999)
    print('Received from %s:%s.' % addr)
    s.sendto(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'),addr)



