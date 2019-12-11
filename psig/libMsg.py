#!/usr/bin/env python3

import json

class MSG(object):
    '''网络消息类型'''
    def GetDict(self):
        return self.__dict__


class Package(object):
    '''网络消息封装'''
    def __init__(self,code,msg:MSG):
        super().__init__()
        self.code=code
        self.msg=msg.GetDict()

    def Value(self):
        return json.dumps(self.__dict__).encode()


# CLASS_PACKAGE_END


class Msg0(MSG):
    '''
    重置与生成密钥
    C -> S
    '''
    def __init__(self,uuidNew,keypub,uuidOld=None):
        super().__init__()
        self.uuidNew=uuidNew
        self.keypub=keypub
        if uuidOld:
            self.uuidOld=uuidOld

class Msg1(MSG):
    '''
    删除代理
    C -> S
    '''

    def __init__(self,ouuid,suuid):
        super().__init__()
        self.ouuid=ouuid
        self.suuid=suuid


class Msg10(MSG):
    '''
    请求代理
    C -> S -> C
    '''
    def __init__(self,ouuid,suuid,nonce):
        super().__init__()
        self.ouuid=ouuid
        self.suuid=suuid
        self.nonce=nonce

class Msg11(MSG):
    '''
    请求应答
    C -> S -> C
    '''
    def __init__(self,ouuid,suuid,nonce,agree=False,keypub=None):
        super().__init__()
        self.ouuid=ouuid
        self.suuid=suuid
        self.nonce=nonce
        self.agree=agree
        if agree:
            self.keypub=keypub


class Msg100(MSG):
    '''
    查询代理
    C -> S
    '''
    def __init__(self,ouuid,suuid):
        super().__init__()
        self.ouuid=ouuid
        self.suuid=suuid

class Msg101(MSG):
    '''
    查询代理结果
    S -> C
    '''
    def __init__(self,ouuid,btime,dtime,keypub,suuid):
        super().__init__()
        self.ouuid=ouuid
        self.suuid=suuid
        self.btime=btime
        self.dtime=dtime
        self.keypub=keypub

class Msg1000(MSG):
    '''登录'''
    def __init__(self,uuid):
        super().__init__()
        self.uuid=uuid

# CLASS_PACKAGE_END