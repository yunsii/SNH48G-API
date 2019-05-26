# 打卡

## 接口

POST

https://puser.48.cn/usersystem/api/user/v1/check/in

### 请求头

```python
{
    "Host": "puser.48.cn",
    "version": "5.0.1",
    "os": "android",
    "Accept-Encoding": "gzip",
    "IMEI": "866716037125810",
    "User-Agent": "Mobile_Pocket",
    "Content-Length": "2",
    "Connection": "Keep-Alive",
    "Content-Type": "application/json;charset=utf-8",
    "token": "{token}"
}
```

### 表单

```python
{}
```

抓包测试发现为空表单post请求

### 响应

#### 成功

```python
{
    "status": 200,
    "message": "success",
    "content": {
        "addEx": 2,
        "addMoney": 10,
        "days": 2
    }
}
```

#### 重复请求

```python
{
    "status": 1001006,
    "message": "今日已签到"
}
```
