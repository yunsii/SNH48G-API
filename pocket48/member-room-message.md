# 成员房间消息

API:

https://pjuju.48.cn/imsystem/api/im/v1/member/room/message/mainpage

## 请求头：
```python
{
        # 'Host': 'pjuju.48.cn',
        # 'version': '5.0.1',
        # 'os': 'android',
        # 'Accept-Encoding': 'gzip',
        # 'IMEI': '866341038102845',
        # 'User-Agent': 'Mobile_Pocket',
        # 'Content-Length': '67',
        # 'Connection': 'Keep-Alive',
        'Content-Type': 'application/json;charset=utf-8',
        'token': {token}
    }
```

## 已知请求参数说明：
名称 | 类型 | 说明 | 必填 | 默认值 | 备注
------- | -------- | ---- | ---- | ----- | ----
Content-Type | str | 接收类型 | Y |  | 
token | str |  | Y |  | 登录后获取

## 表单数据：
```python
{
    "lastTime": 0,
    "limit": {limit},
    "chatType": 0,
    "roomId": {room_id}
}
```

## 已知表单参数说明：
名称 | 类型 | 说明 | 必填 | 默认值 | 备注
------- | -------- | ---- | ---- | ----- | ----
limit | int/str | 消息限制 | Y |  | 
roomId | int/str | 成员房间id | Y |  | 

## 响应：

### 成功：

####
```python
{
    "status": 200,
    "message": "success",
    "content": {
        "data": [
            {
                "msgidClient": "caeef5fe-5ddd-492b-b1d0-fd1a8824f3bc",
                "msgTime": 1535860396835,
                "msgTimeStr": "2018-09-02 11:53:16",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": {
                    "senderAvatar": "/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg",
                    "senderLevel": "B",
                    "roomType": 1,
                    "senderId": 63549,
                    "version": "2.2.5",
                    "contentType": 1,
                    "source": "juju",
                    "fromApp": 2,
                    "phoneName": "iPhone X",
                    "platform": "ios",
                    "sourceId": "5778530",
                    "senderHonor": "",
                    "text": "丑君纪念日，绝版丑君",
                    "role": 2,
                    "phoneSystemVersion": "11.4.1",
                    "messageObject": "text",
                    "senderName": "陈美君",
                    "senderRole": 1,
                    "build": 21100
                }
            },
            {
                "msgidClient": "cf491c54-e40a-4308-93d9-db8e6062066b",
                "msgTime": 1535860220895,
                "msgTimeStr": "2018-09-02 11:50:20",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": {
                    "senderAvatar": "/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg",
                    "senderLevel": "B",
                    "roomType": 1,
                    "senderId": 63549,
                    "version": "2.2.5",
                    "contentType": 1,
                    "source": "juju",
                    "fromApp": 2,
                    "phoneName": "iPhone X",
                    "platform": "ios",
                    "sourceId": "5778530",
                    "senderHonor": "",
                    "text": "今天是丑君",
                    "role": 2,
                    "phoneSystemVersion": "11.4.1",
                    "messageObject": "text",
                    "senderName": "陈美君",
                    "senderRole": 1,
                    "build": 21100
                }
            },
            {
                "msgidClient": "5025ed6c-e53a-4185-9076-174a7bca3405",
                "msgTime": 1535851059228,
                "msgTimeStr": "2018-09-02 09:17:39",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": {
                    "source": "juju",
                    "fromApp": 2,
                    "messageObject": "faipaiText",
                    "senderAvatar": "/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg",
                    "faipaiContent": "早上好！我今天终于18岁啦(๑´ㅂ`๑)",
                    "phoneName": "iPhone X",
                    "senderHonor": "",
                    "messageText": "🌻美好",
                    "senderName": "陈美君",
                    "senderId": 63549,
                    "version": "2.2.5",
                    "senderRole": 1,
                    "build": 21100,
                    "platform": "ios",
                    "roomType": 1,
                    "sourceId": "5778530",
                    "contentType": 1,
                    "faipaiUserId": 546455,
                    "role": 2,
                    "senderLevel": "B",
                    "phoneSystemVersion": "11.4.1"
                }
            },
            {
                "msgidClient": "ae30b75a-5fe3-444f-8047-efc389e13ce3",
                "msgTime": 1535809255851,
                "msgTimeStr": "2018-09-01 21:40:55",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": {
                    "senderAvatar": "/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg",
                    "senderLevel": "B",
                    "roomType": 1,
                    "senderId": 63549,
                    "version": "2.2.5",
                    "contentType": 1,
                    "source": "juju",
                    "fromApp": 2,
                    "phoneName": "iPhone X",
                    "platform": "ios",
                    "sourceId": "5778530",
                    "senderHonor": "",
                    "text": "今天居然是九月一！",
                    "role": 2,
                    "phoneSystemVersion": "11.4.1",
                    "messageObject": "text",
                    "senderName": "陈美君",
                    "senderRole": 1,
                    "build": 21100
                }
            },
            {
                "msgidClient": "fbbc5801-7f22-46d4-8b3a-0d718a7e98d0",
                "msgTime": 1535801348954,
                "msgTimeStr": "2018-09-01 19:29:08",
                "userId": 0,
                "msgType": 0,
                "bodys": "正在直播",
                "extInfo": {
                    "source": "juju",
                    "fromApp": 2,
                    "senderAvatar": "http://www.bej48.com/images/member/zp_20001.jpg?ram=1523268267365",
                    "senderId": "63549",
                    "senderName": "陈美君",
                    "role": 2,
                    "senderLevel": "B",
                    "senderRole": 2,
                    "platform": "server",
                    "roomType": 1,
                    "sourceId": "5778530",
                    "contentType": 1,
                    "messageObject": "live",
                    "referenceTitle": "陈美君的直播间",
                    "referenceContent": "小会儿",
                    "referencecoverImage": "/mediasource/live/1535801343816Lvyb88c4TJ.jpg",
                    "referenceObjectId": "5b8a77ff0cf2234479b4cc64"
                }
            },
            {
                "msgidClient": "9a1b252c-894c-4e4b-bfbd-a27ab2caaae0",
                "msgTime": 1535698873869,
                "msgTimeStr": "2018-08-31 15:01:13",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": {
                    "senderAvatar": "/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg",
                    "senderLevel": "B",
                    "roomType": 1,
                    "senderId": 63549,
                    "version": "2.2.5",
                    "contentType": 1,
                    "source": "juju",
                    "fromApp": 2,
                    "phoneName": "iPhone X",
                    "platform": "ios",
                    "sourceId": "5778530",
                    "senderHonor": "",
                    "text": "有时候会偷偷跑出来一个人的静谧时光😎ི",
                    "role": 2,
                    "phoneSystemVersion": "11.4.1",
                    "messageObject": "text",
                    "senderName": "陈美君",
                    "senderRole": 1,
                    "build": 21100
                }
            },
            {
                "msgidClient": "961ac1fe-737e-47e7-bc0d-044b9213c187",
                "msgTime": 1535698693155,
                "msgTimeStr": "2018-08-31 14:58:13",
                "userId": 0,
                "msgType": 1,
                "bodys": {
                    "size": 476042,
                    "ext": "jpg",
                    "w": 3072,
                    "url": "https://nos.netease.com/nim/NDA5MzEwOA==/bmltYV8xNzc5NDU5MjRfMTUzNTYxNDQ3MTY3N182M2M4MWRlNC1mMDJkLTQ5ODUtYjE2Mi05MDM0MGZhMGFkNDE=",
                    "md5": "e4224a36061c8cb2fdc20e90c5ac037a",
                    "h": 2304
                },
                "extInfo": {
                    "senderAvatar": "/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg",
                    "senderLevel": "B",
                    "roomType": 1,
                    "senderId": 63549,
                    "version": "2.2.5",
                    "contentType": 1,
                    "source": "juju",
                    "fromApp": 2,
                    "phoneName": "iPhone X",
                    "platform": "ios",
                    "sourceId": "5778530",
                    "senderHonor": "",
                    "role": 2,
                    "phoneSystemVersion": "11.4.1",
                    "messageObject": "image",
                    "senderName": "陈美君",
                    "senderRole": 1,
                    "build": 21100
                }
            },
            {
                "msgidClient": "f669e147-101f-46d9-aa93-f970cbd268fe",
                "msgTime": 1535698680635,
                "msgTimeStr": "2018-08-31 14:58:00",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": {
                    "senderAvatar": "/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg",
                    "senderLevel": "B",
                    "roomType": 1,
                    "senderId": 63549,
                    "version": "2.2.5",
                    "contentType": 1,
                    "source": "juju",
                    "fromApp": 2,
                    "phoneName": "iPhone X",
                    "platform": "ios",
                    "sourceId": "5778530",
                    "senderHonor": "",
                    "text": "咖啡店偶遇了田姝丽，她不要脸地坐到我前面💅🏾",
                    "role": 2,
                    "phoneSystemVersion": "11.4.1",
                    "messageObject": "text",
                    "senderName": "陈美君",
                    "senderRole": 1,
                    "build": 21100
                }
            },
            {
                "msgidClient": "f6a8ccf1-87e4-49ea-bbe5-d50d8f1d375e",
                "msgTime": 1535684261213,
                "msgTimeStr": "2018-08-31 10:57:41",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": {
                    "source": "juju",
                    "fromApp": 2,
                    "messageObject": "faipaiText",
                    "senderAvatar": "/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg",
                    "faipaiContent": "美君今天吃八喜了吗",
                    "phoneName": "iPhone X",
                    "senderHonor": "",
                    "messageText": "昨晚梦见战争了。整个梦境很紧张很灰暗，我梦见我走进一家便利店，打开冰箱发现草莓味的八喜，欢喜的带走了。",
                    "senderName": "陈美君",
                    "senderId": 63549,
                    "version": "2.2.5",
                    "senderRole": 1,
                    "build": 21100,
                    "platform": "ios",
                    "roomType": 1,
                    "sourceId": "5778530",
                    "contentType": 1,
                    "faipaiUserId": 358845,
                    "role": 2,
                    "senderLevel": "B",
                    "phoneSystemVersion": "11.4.1"
                }
            },
            {
                "msgidClient": "396f305f-d0cb-45f9-b01e-e5e5ce4323c7",
                "msgTime": 1535684087660,
                "msgTimeStr": "2018-08-31 10:54:47",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": {
                    "senderAvatar": "/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg",
                    "senderLevel": "B",
                    "roomType": 1,
                    "senderId": 63549,
                    "version": "2.2.5",
                    "contentType": 1,
                    "source": "juju",
                    "fromApp": 2,
                    "phoneName": "iPhone X",
                    "platform": "ios",
                    "sourceId": "5778530",
                    "senderHonor": "",
                    "text": "忘了自己拔牙的事儿了。刚刚疯狂舞蹈了整场公演😎ི",
                    "role": 2,
                    "phoneSystemVersion": "11.4.1",
                    "messageObject": "text",
                    "senderName": "陈美君",
                    "senderRole": 1,
                    "build": 21100
                }
            }
        ],
        "lastTime": 1535684087660
    }
}
```

已知**messageObject**:

| 序号 | 名称 | 说明 |
| ---- | --- | ---- |
| 1 | faipaiText | 翻牌 |
| 2 | text | 文本消息 | 
| 3 | image | 图片分享 |
| 4 | idolFlip | 提问信息翻牌，仅直接显示成员回复 |
| 5 | live | 视频直播 |
| 6 | diantai | 电台直播 |

关于**role**（猜测）:

**senderRole** == 1 表示房主（成员），在**extInfo**中，**role** == 0 时，表示另一成员的留言；**role** == 2 时，表示成员的留言。
