#!/usr/bin/env python3

import socket
import threading
import json

from libMsg import *


DBG=True
BUF_SIZE=0x1024
time_s=1562162425.652096 #2019年7月3日

threads=[]
#ip='10.6.64.99'
ip='192.168.123.244'
port=14145

class ClientHandle(object):
    ''''''
    def __init__(self,ip,port):
        super().__init__()
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((ip,port))
        self.input=[self.sock]

    def Send(self,data):
        self.sock.sendall(data)
    
    def Recv(self):
        data=self.sock.recv(BUF_SIZE)
        return data



class Sock(object):
    '''本地socket服务'''
    def __init__(self):
        super().__init__()
        try:
            self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            if DBG == False:
                self.sock.connect((ip,port))
            self.connected=True
            print('连接成功')
        except socket.error as e:
            self.connected=False
            print(e)

    def __del__(self):
        self.sock.close()

    def Send(self,pack:bytes):
        if DBG == False:
            if self.connected:
                try:
                    self.sock.sendall(pack)
                    return json.loads(self.sock.recv(BUF_SIZE))
                except socket.error as e:
                    print(e)
            else:
                return None
        else:
            return self.__handle__(pack)
    
    def __parse__(self,pack:bytes):
        pkg=json.loads(pack)
        code=pkg['code']
        msg=pkg['msg']

        # 非代理请求消息(0b10, 0b11)直接返回
        if code == 0b10:
            pass
        elif code == 0b11:
            pass
        else:
            return pack


    def __handle__(self,pack:bytes):
        with open('key.pem','r') as key_f:
            #key_d=pickle.load(key_f)
            key=json.load(key_f)
        pack=json.loads(pack)
        code=pack['code']
        msg=pack['msg']
        
        if code == 0b100:
            if 'suuid' not in msg:
                responce=Msg101(key['uuid'],time_s,0,key['keypub'])
            else:
                responce=Msg101(key['uuid'],time_s,0,key['keypub'],key['uuid'])
            #pack=package(0b101,responce.__dict__)
            return Package(0b101,responce).__dict__
        return

        if code == 0:
            pass

        if code == 0b10:
            # 转发给代理人
            pass

        if code == 0b11:
            pass

# CLASS_SOCK_END


if __name__ == "__main__":
    sock=ClientHandle(ip,port)
    send=threading.Thread(target=sock)
    send.start()
    pass
