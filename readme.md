# 课程设计

## with python==3.7 pyqt==5.9.2

##接口设计（以下交互接口封装在api.py）
### 信息TAB
1. 新建密钥
```
GenKey(passwd: bytes) => key(密钥)
```
2. 重置密钥：
```
ResetKey(oldPasswd:bytes, newPasswd:bytes) => key(新密钥)
```
3. 获取密钥：客户端启动时加载本地已有密钥
```
GetKey() => key(本地密钥)
```
4. 信息显示：
```
GetInfo() => (版本号、作者、工作目录、其他信息)
```

### 签名
1. 获取签名人列表
```
GetUserList() => userList(所有用户uuid的列表)
```

2. 生成签名
```
Signature(filename,signame,ouuid) => status_code
```

3.获取代理人
```
GetCurrentAgent() => Agent(uuid)
```

### 验证
1. 验证文件签名是否正确
```
Verify(filename,signame) => bool
```

### 代理
1. 新建代理
```python
# 待定
```

2. 撤销授权
```python
# 待定
```
3.获取公钥
```
getPublicKeyByUuid => pubkey:str
```