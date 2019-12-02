# !/usr/bin/env python3
# 密钥操作模块

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_v1_5 as PKCS_Cipher
from Crypto.Signature import pkcs1_15 as PKCS_Sign
from Crypto.Hash import SHA1,MD5

import uuid
import json
import base64

def GetPasswd() -> bytes:
    '''用户输入私钥保护口令'''
    print("输入私钥保护口令: ",end='')
    return b'dlub2040'
    #return input().encode()


def En_key(passwd:bytes,key:bytes) -> bytes:
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


def De_key(passwd:bytes,key:bytes) -> bytes:
    '''解密私钥'''
    #将口令用作私钥的加密密钥
    try:
        md5=MD5.new()
        md5.update(passwd)
        hash=md5.hexdigest().encode()
        aes=AES.new(hash,AES.MODE_ECB)
        mKey=aes.decrypt(key)
        mKey=mKey.strip()
        if hash==mKey[-32:]:
            return mKey[:-32]
    except Exception:
        pass
    return None

def WriteKey(key_d):
    '''写入密钥文件'''
    with open('key.pem', 'w') as key_f:
        #key_f.write(str(key_d).replace("'",'"'))
        json.dump(key_d,key_f)
        #pickle.dump(key_d,key_f)
    return

def ReadKey():
    try:
        with open('key.pem','r') as key_f:
            #key_d=eval(key_f.read()) #存在安全问题, 待解决
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
        
def GenKey():
    '''生成公私钥对文件'''
    id=str(uuid.uuid1()).encode()
    #passwd = GetPasswd()
    passwd=b'dlub2040'

    #生成公私钥对
    rsa=RSA.generate(1024)
    pem=rsa.exportKey('PEM')
    pubkey=rsa.publickey().exportKey('OpenSSH')

    '''
    #将口令用作私钥的加密密钥
    md5=MD5.new()
    md5.update(passwd)
    hash=md5.hexdigest().encode()
    aes=AES.new(hash,AES.MODE_CFB)

    #加密私钥, 绑定口令
    mKey=pem+hash
    mod16=len(mKey)%16
    if mod16:
        mKey+=b' '*(16-mod16)
    cKey=aes.encrypt(mKey)
    '''
    cKey=En_key(passwd,pem)
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
    '''
    #写入私钥文件
    with open('key.pem', 'w') as key_f:
        #key_f.write(str(key_d).replace("'",'"'))
        json.dump(key_d,key_f)
        #pickle.dump(key_d,key_f)
    '''
    return key_d

def Reset(OldKey):
    '''重置密钥'''
    if De_key(GetPasswd(),OldKey):
        key_d = GenKey()
        WriteKey(key_d)
        return key_d
        
if __name__=='__main__':
    print(GenKey()['uuid'])