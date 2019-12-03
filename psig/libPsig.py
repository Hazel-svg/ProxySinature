# !/usr/bin/env python3
# 本文件为主进程文件

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS_Cipher
from Crypto.Signature import pkcs1_15 as PKCS_Sign
from Crypto.Hash import SHA1

import base64
import time
import json

from psig import libList, libKey, libSock, init

# 版本及相关信息
version='0.99-insider'

def Signature(filename,signame,ouuid):
    '''签名函数'''

    '''
    #passwd=libKey.GetPasswd()
    passwd=b'dlub2040'
    key=libKey.De_key(passwd,cKey)
    if key==b'':
        return 0x4001
    if isSelf:
        suuid=ouuid
    else:
        # 查询客户(ouuid)表
        suuid=libList.FindClient(ouuid)
        if not suuid:
            return 0x4F03
    '''
    suuid=libList.IdList.Host['uuid']
    siger=libList.FindClient(ouuid)
    if not siger:
        return 0x4F03
    cKey = siger['key']

    passwd=libKey.GetPasswd()
    #passwd=b'dlub2040'
    key=libKey.De_key(passwd,base64.b64decode(cKey))
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
        #sig=libSign.Sign(RSA.importKey(key),SHA1.new(str(sig_d['hash']+sig_d['time']+sig_d['ouuid']+sig_d['suuid']).encode()))
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

def Verify(filename,signame,sock):
    '''签名验证函数'''
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
    msg1=libSock.type100(sig_d['ouuid'],sig_d['suuid'])
    res=json.loads(libSock.Send(0b100,msg1,sock))

    if 'msg' not in res:
        return 0x4F03

    Siger=res['msg']


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

if __name__=='__main__':
    key=init.check()
    server=libSock.ClientServer()
    print(key['uuid'])
    #if Signature('readme.txt','readme.txt.psig',key['uuid']) == 0:
    #    print('\n签名成功')
    if Verify('psig/readme.txt','psig/readme.txt.psig', server) == 0:
        print('签名验证正确')
