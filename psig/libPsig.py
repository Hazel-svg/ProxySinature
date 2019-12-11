#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_v1_5 as PKCS_Cipher
from Crypto.Signature import pkcs1_15 as PKCS_Sign
from Crypto.Hash import SHA1,MD5
from Crypto.Random import random

import uuid
import json
import base64
import time
import socket
import select
import threading

from psig.libMsg import *
#from libSock import *

BUF_SIZE=0x1024
ip='35.194.227.136'
port=14145

#query=None

def ReadKey():
    try:
        with open('key.pem','r') as key_f:
            #key_d=pickle.load(key_f)
            key_d=json.load(key_f)
            
            KeyPub=RSA.importKey(key_d['keypub'])

            key_header=key_d['uuid']+key_d['key']+key_d['keypub']
            hash_header=SHA1.new(key_header.encode())

            #验证签名
            cipher=PKCS_Sign.new(KeyPub)
            cipher.verify(hash_header,base64.b64decode(key_d['headersig']))
        return key_d
    except BaseException:
        return None



class Sock(object):
    def __init__(self):
        super().__init__()
        self.uuid=ReadKey()['uuid']
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((ip,port))
        self.input=[self.sock]
        loginmsg=Msg1000(self.uuid)
        pack=Package(0b1000,loginmsg)
        self.sock.sendall(pack.Value())
        self.l=threading.Thread(target=self.Recv,args=())
        self.l.start()
        self.query=None
        self.agentmsg=None
        

    def __del__(self):
        self.l._stop()
        self.sock.close()


    def Send(self,data:bytes):
        self.sock.sendall(data)
    
    def Recv(self):
        #global query
        while True:
            data=self.sock.recv(BUF_SIZE)
            pack=json.loads(data)
            code=pack['code']
            msg=pack['msg']
            if code==0b10:
                # 请求代理
                agree,passwd=IsAcc(msg['ouuid'])
                if agree:
                    skey=Key(uuid=msg['ouuid'],key=None,passwd=passwd)
                    # 更新ClientList

                res=Msg11(msg['ouuid'],msg['suuid'],msg['nonce'],agree,skey.key['keypub'] if agree else None)
                res_p=Package(0b11,res)
                self.sock.sendall(res_p.Value())
            elif code==0b11:
                if msg['agree']:
                    # 更新AgentList
                    self.agentmsg=msg
            elif code==0b101:
                self.query=data

# CLASS_SOCK_END

class Key(object):

    def __init__(self,uuid=None,key=None,passwd=None): # 密码需手动输入, 此处为方便调试
        super().__init__()
        if key:
            self.key=key
            return
        #self.key=self.ReadKey()
        #passwd= #此处应弹出输入框
        if passwd:
            self.key=self.GenKey(passwd)
            if  uuid:
                self.key['uuid']=uuid
                return
            self.WriteKey(self.key)
    
    def WriteKey(self,key):
        '''写入密钥文件'''
        with open('key.pem', 'w') as key_f:
            #key_f.write(str(key_d).replace("'",'"'))
            json.dump(key,key_f)
            #pickle.dump(key_d,key_f)
        return


    def __str__(self):
        return json.dumps(self.key)


    def GenKey(self,passwd:bytes):
        '''生成公私钥对文件'''
        id=str(uuid.uuid1()).encode()
        #passwd = GetPasswd()
        #passwd=

        #生成公私钥对
        rsa=RSA.generate(1024)
        pem=rsa.exportKey('PEM')
        pubkey=rsa.publickey().exportKey('OpenSSH')

        cKey=self.Enkey(passwd,pem)
        #生成dict对象
        key_d=dict()
        key_d['uuid']=str(id,encoding='utf-8')
        key_d['key']=str(base64.b64encode(cKey),encoding='utf-8')
        key_d['keypub']=str(pubkey,encoding='utf-8')

        ##计算私钥头摘要
        key_header=key_d['uuid']+key_d['key']+key_d['keypub']
        #key_header=str(key_d).encode()
        #sha=hashlib.sha1()
        #sha.update(key_header)
        hash_header=SHA1.new(key_header.encode())

        ##使用私钥签名
        sign=PKCS_Sign.new(rsa)
        sig_header=sign.sign(hash_header)
        key_d['headersig']=str(base64.b64encode(sig_header),encoding='utf-8')
        return key_d

    def Enkey(self,passwd:bytes,key:bytes) -> bytes:
        '''加密私钥'''
        #将口令用作私钥的加密密钥
        md5=MD5.new()
        md5.update(passwd)
        hash=md5.hexdigest().encode()
        aes=AES.new(hash,AES.MODE_ECB)

        #加密私钥, 绑定口令
        mKey=key+hash
        mod16=len(mKey)%16
        if mod16:
            mKey+=b' '*(16-mod16)
        cKey=aes.encrypt(mKey)
        return cKey


    def Dekey(self,passwd:bytes) -> bytes:
        '''解密私钥'''
        #将口令用作私钥的加密密钥
        t_key=base64.b64decode(self.key['key'])
        try:
            md5=MD5.new()
            md5.update(passwd)
            hash=md5.hexdigest().encode()
            aes=AES.new(hash,AES.MODE_ECB)
            mKey=aes.decrypt(t_key)
            mKey=mKey.strip()
            if hash==mKey[-32:]:
                return mKey[:-32]
        except Exception:
            pass
        return None

    def Reset(self,oldPasswd,newPasswd):
        '''重置密钥'''
        if self.Dekey(oldPasswd):
            self.key=self.GenKey(newPasswd)
            self.WriteKey(self.key)
            return True
        else:
            return False


    def Signature(self,filename,signame,ouuid,client,passwd): # 密码应手动输入, 此处为方便调试
        '''签名函数'''
        suuid=client.host['uuid']
        siger=Key(uuid=None,key=client.Find(ouuid))
        if not siger:
            return 0x4F03

        #passwd=
        key=siger.Dekey(passwd)
        if not key:
            return 0x4001

        try:
            f=open(filename,'rb')
            Hash=SHA1.new(f.read())
            f.close()
            sig_d=dict()
            sig_d['hash']=Hash.hexdigest()
            sig_d['time']=str(time.time())
            sig_d['ouuid']=ouuid
            sig_d['suuid']=suuid
            cipher=PKCS_Sign.new(RSA.importKey(key))
            sig=cipher.sign(SHA1.new(str(sig_d['hash']+sig_d['time']+sig_d['ouuid']+sig_d['suuid']).encode()))
            sig_d['sig']=str(base64.b64encode(sig),encoding='utf-8')
            with open(signame,'w') as sig_f:
                json.dump(sig_d,sig_f)
            return 0
        except IOError:
            return 0x4011
        except BaseException:
            return 0x4000

    def Verify(self,filename,signame,sock:Sock):
        '''签名验证函数'''
        #global query
        try:
            with open(filename,'rb') as f:
                Hash=SHA1.new(f.read())
            with open(signame,'r') as sig_f:
                sig_d=json.load(sig_f)
        except IOError:
            return 0x4011
        except BaseException:
            return 0x4000
        
        # 文件哈希值是否一致
        if sig_d['hash'] != Hash.hexdigest():
            return 0x4F01

        # UUID是否有效
        '''
        Sigee=libSock.Select(sig_d['ouuid'])
        if not Sigee:
            return 0x4F03
        Siger=libSock.SelectDeal(sig_d['ouuid'],sig_d['suuid'])
        '''
        #msg=init.libSock.type100(sig_d['ouuid'],sig_d['suuid'])
        msg=Msg100(sig_d['ouuid'],sig_d['suuid'])
        pack=Package(0b100,msg)
        sock.sock.sendall(pack.Value())

        res=None
        ts=time.time()
        while time.time()-ts < 10 and not res:
            res=sock.query
        del ts

        sock.query=None
        if  not res:
            return 0x4F03

        Siger=json.loads(res)['msg']


        # 时间戳是否有效
        #live_t=res['live_t']
        #live_t=(0,9999999999)
        #if live_t[0]<float(sig_d['time'])<live_t[1]:
        if (Siger['dtime']==0.0 or float(sig_d['time'])<Siger['dtime']) and Siger['btime']<float(sig_d['time']):
            # KeyPub=Siger.KeyPub
            KeyPub=Siger['keypub']
            try:
                cipher=PKCS_Sign.new(RSA.importKey(KeyPub))
                cipher.verify(SHA1.new(str(sig_d['hash']+sig_d['time']+sig_d['ouuid']+sig_d['suuid']).encode()),base64.b64decode(sig_d['sig']))
            except (ValueError, TypeError):
                return 0x4F04
        else:
            return 0x4F02
        return 0
# CLASS_KEY_END


class UserList(object):
    '''用户列表'''
    host=dict()
    user=dict()
    dit=''

    def __init__(self,k:Key):
        self.host=k.key
        try:
            with open(self.dit,'r') as f:
                self.user=json.load(f)
            self.user[self.host['uuid']]
        except BaseException:
            self.AddUser(self.host['uuid'],self.host)
    
    def __str__(self):
        return json.dumps(self.user)
        #return super.__repr__(self)

    def Find(self,uuid):
        '''查找用户'''
        try:
            return self.user[uuid]
        except BaseException:
            return None
    
    def AddUser(self,uuid,val:dict()):
        '''添加用户'''
        self.user[uuid]=val
        self.Update()

    def Delete(self,uuid):
        '''删除用户'''
        self.user.pop(uuid)
        self.Update()

    def Update(self):
        with open(self.dit,'w') as f:
            json.dump(self.user,f)
    

class AgentList(UserList):
    dit='Agent.dit'

    def __init__(self, k):
        self.host=k.key
        try:
            with open(self.dit,'r') as f:
                self.user=json.load(f)
            self.user[self.host['uuid']]
        except BaseException:
            self.AddUser(self.host['uuid'],{'uuid':self.host['uuid'], 'keypub':self.host['keypub']})
        
class ClientList(UserList):
    dit='Client.dit'

# CLASS_USERLIST_END


def NewAgent(ouuid,suuid,agent:AgentList,sock:Sock):
    '''
    新建代理
    ouuid = 本地用户id
    '''
    nonce=random.getrandbits(32)
    msg=Msg10(ouuid,suuid,nonce)
    pack=Package(0b10,msg)
    sock.Send(pack.Value())

    st=time.time()
    res=None
    while time.time()-st < 10 and res==None:
        res=sock.agentmsg
    
    sock.agentmsg=None

    if res['agree'] and nonce == res['nonce']:
        val={'uuid':res['suuid'],'keypub':res['keypub']}
        al.AddUser(res['suuid'],val)

    #agent.AddUser(suuid)
    return

def DelAgent(ouuid,suuid,agent:AgentList,sock:Sock):
    '''删除代理'''
    agent.Delete(suuid)
    msg=Msg1(ouuid,suuid)
    pack=Package(0b1,msg)
    sock.Send(pack.Value())
    return

def AccAgent(ouuid,suuid,agree,nonce,client:ClientList,sock:Sock):
    '''
    接受代理
    suuid = 本地用户id
    '''
    if not agree: 
        msg=Msg11(ouuid,suuid,nonce)
    else:    
        pKey=Key(uuid=ouuid)
        msg=Msg11(ouuid,suuid,nonce,agree,keypub=pKey.key['keypub'])
        client.AddUser(ouuid,pKey)
    pack=Package(0b11,msg)
    res=sock.Send(pack.Value())

    return

def IsAcc(ouuid):
    '''弹出请求代理对话框'''
    return True,


if __name__=='__main__':
    # 以下为初始化代码
    t=ReadKey()
    if not t:
        key=Key()
    else:
        key=Key(uuid=None,key=t)
    del t
    sock=Sock()
    cl=ClientList(key)
    al=AgentList(key)
    # 初始化完成

    #NewAgent(key.key['uuid'],'02813290-1a86-11ea-bebb-94e6f741055e',al,sock)


    #key.Signature('readme.txt','readme.txt.psig',key.key['uuid'],cl)
    #if not key.Verify('readme.txt','readme.txt.psig',sock): print('验证成功')

