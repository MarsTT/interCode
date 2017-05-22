#coding=utf-8

import socket


'''
	socket 服务器/客户端
		3.1 创建socket对象，socket.socket(arg1,arg2)
			arg1:  1.AF_INEF 或者 AF_UNIX
			arg2:  2.SOCK_STREAM(tcp/ip)    SOCK_DGRAM(udp)

		3.2 绑定端口，socket.bind(('localhost',8888))

		3.3 socket.listen(n)
			n: 代表允许多少个同时请求

		3.4 connection,address = sock.accept()

		3.5 buf = connection.recv(100)

		3.6 connection.send(buf)

		3.7 不关闭就很惨,connection.close()
'''



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8125))
s.listen(8)
while True:
	connection,address = s.accept()
	buf = connection.recv(10)
	connection.send(buf)
s.close()