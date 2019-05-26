# 房间信息

## 接口

POST

https://puser.48.cn//usersystem/api/user/member/v1/fans/room

根据 memberId 获取成员房间基本信息

### 请求头

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

### 表单

```python
{
    "memberId": 63560  # 成员id
}
```

### 响应

```python
{
	"status": 200,
	"message": "success",
	"content": {
		"fansNum": 38845,
		"roomInfo": {
			"roomId": 5778533,
			"roomType": 0,
			"roomName": "哆啦哆啦！",
			"topic": "水獭小宝贝！",
			"hot": 66552,
			"roomAvatar": "/mediasource/room/1525202296034dP68WGWUBy.jpg",
			"memberId": 63560,
			"memberName": "姜杉",
			"disabledJoin": false,
			"disabledMessage": false,
			"groupId": 10,
			"lastCommentInfo": "[街舞][街舞]",
			"lastCommentTime": "2018-10-09 20:45:34",
			"mood": "0",
			"moodName": "",
			"bgPath": "/mediasource/room/1525202296587d1tvPT279v.jpg",
			"fontColor": "0",
			"role": 1,
			"voteMemberId": 10119,
			"topGiftUserId": 874692
		}
	}
}
```
