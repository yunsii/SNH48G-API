# 登录

POST

https://puser.48.cn/usersystem/api/user/v1/login/phone

## 请求头

```python
{
    "Host": "puser.48.cn",
    "version": "5.0.1",
    "os": "android",
    "Accept-Encoding": "gzip",
    "IMEI": "866716037125810",
    "User-Agent": "Mobile_Pocket",
    "Content-Length": "75",
    "Connection": "Keep-Alive",
    "Content-Type": "application/json;charset=utf-8",
    "token": "0"
}
```

## 表单

```python
{
    "latitude": 0,
    "longitude": 0,
    "password": "{password}",
    "account": "{account}"
}
```

## 响应

### 成功

```python
{
    "status": 200,
    "message":"success",
    "content": {
        "userInfo": {
            "userId": 11111,
            "nickName":"xxxxxx",
            "pocketId": "",
            "avatar": "/mediasource/avatar/150393076543045qpl8zce3.png",
            "experience": 1913,
            "level": 5,
            "gender": 2,
            "punchCardDay": 2,
            "birthday": "1111-11-11",
            "role": 0,
            "starwo": False,
            "phoneType": 0
        },
        "token": "xxxxxx",  # 经测试 token 有效期为一个月
        "bindInfo": [
            {
              "type": 0, "thirdName": "XXXXXX"  # 微博
            }, {
              "type": 1, "thirdName": "XXXXXX"  # QQ
            }, {
              "type": 2, "thirdName": "XXXXXX"  # 微信
            }, {
              "type": 4, "thirdName": "XXXXXX"  # 手机
            }, {
              "type": 5, "thirdName": "XXXXXX"  # 百度
            }, {
              "type": 3, "thirdName": "XXXXXX"  # 丝瓜
            }
        ],
        "friends": [5, 28, 45, 63, 1544, 2508, 5566, 49007, 63549, 63554, 63555, 63559, 63560, 63571, 63572, 286977, 327560, 327567, 327569, 327581, 327591, 327596, 327597, 327600, 399669, 407106, 407127, 417320, 417328, 417333, 459999, 460005, 528094, 530452, 538735, 594003, 617948, 652650, 825996],
        "todayPunchCard": True,
        "functionIds": [2001, 1003, 2002, 9001]
    }
}
```
