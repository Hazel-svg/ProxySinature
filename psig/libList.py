# !/usr/bin/env python3
# 代理关系模块

import json

import libSock
import libKey

class List(object):
    '''用户表和代理表'''
    Client=dict()
    Agent=dict()
    Host=libKey.ReadKey()

    def __init__(self):
        super().__init__()
        try:
            with open('Client.dit','r') as c:
                self.Client=json.load(c)
            self.Client[self.Host['uuid']]
        except BaseException:
            self.AddClient(self.Host)

        try:
            with open('Agent.dit','r') as c:
                self.Agent=json.load(c)
            self.Agent[self.Host['uuid']]
        except BaseException:
            self.AddAgent(self.Host['uuid'],self.Host['keypub'])
            #self.UpdateAgent()

            
    def __del__(self):
        #self.UpdateAgent()
        #self.UpdateClient()
        return
    

    def AddClient(self,key):
        self.Client[key['uuid']]=key
        self.UpdateClient()
        return
            
    def AddAgent(self,uuid,keypub):
        key=dict()
        key['uuid']=uuid
        key['keypub']=keypub
        self.Agent[uuid]=key
        self.UpdateAgent()
        return

    def UpdateClient(self):
        with open('Client.dit','w') as f:
            json.dump(self.Client,f)
        return

    def UpdateAgent(self):
        with open('Agent.dit','w') as f:
            json.dump(self.Agent,f)
        return

# End Class List

IdList=List()

def FindClient(ouuid):
    '''查找Client'''
    global IdList
    try:
        return IdList.Client[ouuid]
    except BaseException:
        return None
def FindAgent(suuid):
    '''查找Agent'''
    global IdList
    try:
        return IdList.Agent[suuid]
    except BaseException:
        return None

def NewAgent():
    '''新建代理'''
    return
def DelAgent():
    '''删除代理'''
    return
def AccAgent():
    '''接受代理'''
    return
if __name__=='__main__':
    print(IdList.Host['uuid'])