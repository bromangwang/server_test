#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

# 1、创建服务端的socket对象
sk = socket.socket()

# 2、绑定一个ip和端口
sk.bind(("192.168.0.67",8888))

# 3、服务器端一直监听是否有客户端进行连接
sk.listen(5)

while 1:
    # 4、如果有客户端进行连接、则接受客户端的连接
    conn,addr = sk.accept() # 返回客户端socket通信对象和客户端的ip

    # 5、客户端与服务端进行通信
    rev_data = conn.recv(1024)
    print('服务端收到客户端发来的消息:%s' % (rev_data.decode('GB2312')))

    # 6、服务端给客户端回消息
    conn.send(b"HTTP/1.1 200 OK \r\n\r\n")  #http协议
    show_str = "<h1> 这短短的一生，我们最终都会失去，你不妨大胆一些。爱一个人，攀一座山，追一个梦,加油 !!!</h1>"
    conn.send(show_str.encode('GB2312'))

    # 7、关闭socket对象
    conn.close()