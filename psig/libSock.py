# !/usr/bin/env python3
# 网络通信模块

import socket
import struct
import json

import init
import libDbg

DBG=True

BUF_SIZE=0x1024

class package(object):
    '''网络报文消息'''

    def __init__(self,type=0,msg={}):
        self.type=type
        self.msg=msg
    
    def pack(self,msg):
        self.msg=msg


class type0(object):
    '''重置密钥消息与生成密钥'''
    def __init__(self,uuidNew,keypub,uuidOld=None):
        super().__init__()
        self.uuidNew=uuidNew
        self.keypub=keypub
        if uuidOld:
            self.uuidOld=uuidOld


class type10(object):
    '''请求代理'''
    def __init__(self,ouuid,suuid,nonce):
        super().__init__()
        self.ouuid=ouuid
        self.suuid=suuid
        self.nonce=nonce


class type11(object):
    '''请求应答'''
    def __init__(self,ouuid,suuid,agree=False,keypub=None,nonce=None):
        super().__init__()
        self.ouuid=ouuid
        self.suuid=suuid
        self.agree=agree
        if agree:
            self.keypub=keypub
            self.nonce=nonce


class type100(object):
    '''查询代理'''
    def __init__(self,ouuid,suuid=None):
        super().__init__()
        self.ouuid=ouuid
        if suuid:
            self.suuid=suuid
    

class type101(object):
    '''查询代理结果'''
    def __init__(self,ouuid,btime,dtime,keypub,suuid=None):
        super().__init__()
        self.ouuid=ouuid
        if suuid:
            self.suuid=suuid
        self.btime=btime
        self.dtime=dtime
        self.keypub=keypub
        

def pack2json(package):
    return json.dumps(package.__dict__)

def makemsg(type,msg):
    pack = package(type,msg.__dict__)
    return pack2json(pack)

class ClientServer(object):
    '''本地socket服务器'''
    def __init__(self,host=init.host,port=init.port):
        super().__init__()
        try:
            self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            if DBG == False:
                self.sock.connect((host,port))
            self.connected=True
            print('连接成功')
        except socket.error as e:
            self.connected=False
            print(e)

    def __del__(self):
        self.sock.close()

    def send(self,msg):
        if DBG == False:
            if self.connected:
                try:
                    self.sock.sendall(msg.encode())
                    return self.sock.recv(BUF_SIZE)
                except socket.error as e:
                    print(e)
            else:
                return None
        else:
            return libDbg.handle(msg)

class AccountInfo(object):
    '''账号信息'''
    uuid=''
    btime=0.0
    dtime=0.0
    keypub=''
    def __init__(self):
        super().__init__()
        localkey=init.check()
        self.uuid=localkey['uuid']
        self.keypub=localkey['keypub']

    

def Select(UUID):
    return AccountInfo()

def SelectDeal(ouuid,suuid):
    return AccountInfo()

def Send(type,msg,sock:ClientServer):
    res = sock.send(makemsg(type,msg))
    return res


if __name__=='__main__':
    server=ClientServer()
    key=init.check()
    body=type100(key['uuid'])
    pack=package(0b100,body.__dict__)
    msg = pack2json(pack)
    print(server.send(msg))
    print('exit')