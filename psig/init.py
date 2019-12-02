# !/usr/bin/env python3



import base64
import json

import libKey

host='windofwhite.top'
port=14145

def check():
    '''
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
            
    except BaseException:
        '''
    key_d=libKey.ReadKey()
    if not key_d:
        print('密钥文件错误, 自动重置密钥')
        key_d = libKey.GenKey()
        libKey.WriteKey(key_d)
    
    return key_d

if __name__=='__main__':
    print(check()['uuid'])