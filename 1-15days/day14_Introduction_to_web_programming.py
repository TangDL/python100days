# TCP 协议的三个原则：
#   1.数据不传丢不传错（握手，校验和重传机制）
#   2.流量控制（通过滑动窗口控制数据发送者和接收者之间的传输速度）
#   3.拥塞机制（通过RTT时间以及滑动窗口的控制来缓解网络的拥堵）

# 网络应用模式
#   1.C/S模式和B/S模式
#   2.去中心化的网络应用模式（没有服务器作为中心）

# HTTP协议
#   HTTP协议：超文本传输协议
#   HTTPS协议：超文本安全传输协议
#   是进行网络通信的基础，一种应用层的协议


from time import time
from threading import Thread
import requests
from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

class downloadhanlder(Thread):
    def __init__(self, url):
        super.__init__()
        self.url = url
    def run(self):
        filename = self.url[self.url.refind('/') + 1:]
        resp = requests.get(self.url)
        with open("E:\works\python100days" + filename, 'wb') as fp:
            fp.write(resp.content)

def get_image():
    resp = requests.get('https://huaban.com/pins/1144239751/')
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        downloadhanlder(url).start()

def time_servers():
    # 1.创建套接字对象并指定使用哪一种传输服务
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.绑定IP地址和端口，同一时间只能绑定一个IP地址和端口，否则报错
    server.bind(('192.168.1.2', 6789))
    # 3.开始监听，监听客户端连接到服务器，参数512可以理解为连接队列的大小
    server.listen(512)
    print('服务器启动并开始监听...')
    while 1:
        # 4.通过循环接收客户端的连接并作出相应的处理
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器')
        # 5.发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6.断开连接
        client.close()

def time_client():
    client = socket()
    client.connect(('192.168.1.2', 6789))
    print(client.recv(1024).decode('utf-8'))
    client.close()



def main():
    # get_image()
    time_servers()
    # time_client()

if __name__ =='__main__':
    main()