#! /usr/bin/env python3

'''提供调试时的接口, 模拟服务器通信'''

import json

from psig import init

key=init.check()
time_s=1562162425.652096 #2019年7月3日

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

def handle(msg):
    msg=json.loads(msg)
    ty=msg['type']

    if ty == 0b100:
        if 'suuid' not in msg['msg']:
            responce=type101(key['uuid'],time_s,0,key['keypub'])
        else:
            responce=type101(key['uuid'],time_s,0,key['keypub'],key['uuid'])
        #pack=package(0b101,responce.__dict__)
    return makemsg(0b101,responce)

    if ty == 0:
        pass

    if ty == 0b10:
        pass

    if ty == 0b11:
        pass

if __name__=='__main__':
    pass
    print(time_s)