# 用户相关信息

POST

https://puser.48.cn/usersystem/api/user/v1/login/{user_id}

**注意**：该API链接需要替换占位符为登录时获取的本用户id

## 请求头

```python
{
    "Host": "puser.48.cn",
    "version": "5.0.1",
    "os": "android",
    "Accept-Encoding": "gzip",
    "IMEI": "866716037125810",
    "User-Agent": "Mobile_Pocket",
    "Content-Length": "67",
    "Connection": "Keep-Alive",
    "Content-Type": "application/json;charset=utf-8",
    "token": "{token}"
}
```

## 表单

```python
{}
```

## 响应

### 成功

```python
{
	"status": 200,
	"message": "success",
	"content": {
		"userInfo": {
			"userId": 11111,
			"nickName": "XXXXXX",
			"pocketId": "",
			"avatar": "XXXXXX.png",
			"experience": 1111,
			"level": 1,
			"gender": 1,
			"punchCardDay": 0,
			"birthday": "1111-11-11",
			"role": 0,
			"starwo": false,
			"phoneType": 0
		},
		"friendsNum": 0
	}
}
```
