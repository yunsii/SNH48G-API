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
                "msgidClient": "823d8d70-91d9-44ee-a24b-80f83dd4e4d2",
                "msgTime": 1535431471335,
                "msgTimeStr": "2018-08-28 12:44:31",
                "userId": 0,
                "msgType": 1,
                "bodys": "{\"size\":773736,\"ext\":\"jpg\",\"w\":3024,\"url\":\"https://nos.netease.com/nim/NDA5MzEwOA==/bmltYV8xNzc5NDU5MjRfMTUyODk1MDU0MzM4Nl8zYzNmYTIwNS1mYTBhLTQzYzAtODBkYi1hMDg3NjMxNjcyYTg=\",\"md5\":\"680401f92c18a68286832f2c832e776e\",\"h\":3024}",
                "extInfo": "{\"senderAvatar\":\"/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg\",\"senderLevel\":\"B\",\"roomType\":1,\"senderId\":63549,\"version\":\"2.2.5\",\"contentType\":1,\"source\":\"juju\",\"fromApp\":2,\"phoneName\":\"iPhone X\",\"platform\":\"ios\",\"sourceId\":\"5778530\",\"senderHonor\":\"\",\"role\":2,\"phoneSystemVersion\":\"11.4.1\",\"messageObject\":\"image\",\"senderName\":\"陈美君\",\"senderRole\":1,\"build\":21100}"
            },
            {
                "msgidClient": "5926ae42-4ea6-4950-8bde-7d6f8fe63df4",
                "msgTime": 1535427838053,
                "msgTimeStr": "2018-08-28 11:43:58",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": "{\"senderAvatar\":\"/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg\",\"senderLevel\":\"B\",\"roomType\":1,\"senderId\":63549,\"version\":\"2.2.5\",\"contentType\":1,\"source\":\"juju\",\"fromApp\":2,\"phoneName\":\"iPhone X\",\"platform\":\"ios\",\"sourceId\":\"5778530\",\"senderHonor\":\"\",\"text\":\"完了，有人来给我擦口水吗\",\"role\":2,\"phoneSystemVersion\":\"11.4.1\",\"messageObject\":\"text\",\"senderName\":\"陈美君\",\"senderRole\":1,\"build\":21100}"
            },
            {
                "msgidClient": "b71f412e-ddaf-4433-b286-5062514dbc79",
                "msgTime": 1535427570036,
                "msgTimeStr": "2018-08-28 11:39:30",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": "{\"senderAvatar\":\"/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg\",\"senderLevel\":\"B\",\"roomType\":1,\"senderId\":63549,\"version\":\"2.2.5\",\"contentType\":1,\"source\":\"juju\",\"fromApp\":2,\"phoneName\":\"iPhone X\",\"platform\":\"ios\",\"sourceId\":\"5778530\",\"senderHonor\":\"\",\"text\":\"医生的头顶仿佛有光，我看见了天使\",\"role\":2,\"phoneSystemVersion\":\"11.4.1\",\"messageObject\":\"text\",\"senderName\":\"陈美君\",\"senderRole\":1,\"build\":21100}"
            },
            {
                "msgidClient": "9241802b-d0bc-4753-81e9-659342945995",
                "msgTime": 1535427542510,
                "msgTimeStr": "2018-08-28 11:39:02",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": "{\"senderAvatar\":\"/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg\",\"senderLevel\":\"B\",\"roomType\":1,\"senderId\":63549,\"version\":\"2.2.5\",\"contentType\":1,\"source\":\"juju\",\"fromApp\":2,\"phoneName\":\"iPhone X\",\"platform\":\"ios\",\"sourceId\":\"5778530\",\"senderHonor\":\"\",\"text\":\"很迅速又轻松\",\"role\":2,\"phoneSystemVersion\":\"11.4.1\",\"messageObject\":\"text\",\"senderName\":\"陈美君\",\"senderRole\":1,\"build\":21100}"
            },
            {
                "msgidClient": "0938ad3e-cdb0-479b-a222-ab5b2742db68",
                "msgTime": 1535427466482,
                "msgTimeStr": "2018-08-28 11:37:46",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": "{\"senderAvatar\":\"/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg\",\"senderLevel\":\"B\",\"roomType\":1,\"senderId\":63549,\"version\":\"2.2.5\",\"contentType\":1,\"source\":\"juju\",\"fromApp\":2,\"phoneName\":\"iPhone X\",\"platform\":\"ios\",\"sourceId\":\"5778530\",\"senderHonor\":\"\",\"text\":\"我拔完了\",\"role\":2,\"phoneSystemVersion\":\"11.4.1\",\"messageObject\":\"text\",\"senderName\":\"陈美君\",\"senderRole\":1,\"build\":21100}"
            },
            {
                "msgidClient": "1414b299-1232-4ac1-bc3f-85a781a7e90a",
                "msgTime": 1535427459777,
                "msgTimeStr": "2018-08-28 11:37:39",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": "{\"senderAvatar\":\"/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg\",\"senderLevel\":\"B\",\"roomType\":1,\"senderId\":63549,\"version\":\"2.2.5\",\"contentType\":1,\"source\":\"juju\",\"fromApp\":2,\"phoneName\":\"iPhone X\",\"platform\":\"ios\",\"sourceId\":\"5778530\",\"senderHonor\":\"\",\"text\":\"啊啊啊\",\"role\":2,\"phoneSystemVersion\":\"11.4.1\",\"messageObject\":\"text\",\"senderName\":\"陈美君\",\"senderRole\":1,\"build\":21100}"
            },
            {
                "msgidClient": "a7e0aac0-8b34-49b1-b0d7-457bc45198ce",
                "msgTime": 1535424655358,
                "msgTimeStr": "2018-08-28 10:50:55",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": "{\"senderAvatar\":\"/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg\",\"senderLevel\":\"B\",\"roomType\":1,\"senderId\":63549,\"version\":\"2.2.5\",\"contentType\":1,\"source\":\"juju\",\"fromApp\":2,\"phoneName\":\"iPhone X\",\"platform\":\"ios\",\"sourceId\":\"5778530\",\"senderHonor\":\"\",\"text\":\"🤣ok的\",\"role\":2,\"phoneSystemVersion\":\"11.4.1\",\"messageObject\":\"text\",\"senderName\":\"陈美君\",\"senderRole\":1,\"build\":21100}"
            },
            {
                "msgidClient": "b9c8b23b-6950-4fe7-b656-16dc106329da",
                "msgTime": 1535424638917,
                "msgTimeStr": "2018-08-28 10:50:38",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": "{\"senderAvatar\":\"/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg\",\"senderLevel\":\"B\",\"roomType\":1,\"senderId\":63549,\"version\":\"2.2.5\",\"contentType\":1,\"source\":\"juju\",\"fromApp\":2,\"phoneName\":\"iPhone X\",\"platform\":\"ios\",\"sourceId\":\"5778530\",\"senderHonor\":\"\",\"text\":\"一个人去了，工作日大家都忙\",\"role\":2,\"phoneSystemVersion\":\"11.4.1\",\"messageObject\":\"text\",\"senderName\":\"陈美君\",\"senderRole\":1,\"build\":21100}"
            },
            {
                "msgidClient": "32b72d28-8e94-4a12-85da-946debd6bc0e",
                "msgTime": 1535379279947,
                "msgTimeStr": "2018-08-27 22:14:39",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": "{\"senderAvatar\":\"/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg\",\"senderLevel\":\"B\",\"roomType\":1,\"senderId\":63549,\"version\":\"2.2.5\",\"contentType\":1,\"source\":\"juju\",\"fromApp\":2,\"phoneName\":\"iPhone X\",\"platform\":\"ios\",\"sourceId\":\"5778530\",\"senderHonor\":\"\",\"text\":\"昨天吃饭的时候隔壁桌坐着火箭少女的人气成员，就看过一集也不知道为啥我眼睛这么尖。嗷哇，北京有点小。突然觉得人家皮肤好好，自己像刚务农了的一样😎ི\",\"role\":2,\"phoneSystemVersion\":\"11.4.1\",\"messageObject\":\"text\",\"senderName\":\"陈美君\",\"senderRole\":1,\"build\":21100}"
            },
            {
                "msgidClient": "90e58c43-1a91-4bbc-ac2e-160c65f13109",
                "msgTime": 1535379107049,
                "msgTimeStr": "2018-08-27 22:11:47",
                "userId": 0,
                "msgType": 0,
                "bodys": "",
                "extInfo": "{\"senderAvatar\":\"/mediasource/avatar/20180505/1525490672019vhaUovXM26.jpg\",\"senderLevel\":\"B\",\"roomType\":1,\"senderId\":63549,\"version\":\"2.2.5\",\"contentType\":1,\"source\":\"juju\",\"fromApp\":2,\"phoneName\":\"iPhone X\",\"platform\":\"ios\",\"sourceId\":\"5778530\",\"senderHonor\":\"\",\"text\":\"那个，分享个事儿\",\"role\":2,\"phoneSystemVersion\":\"11.4.1\",\"messageObject\":\"text\",\"senderName\":\"陈美君\",\"senderRole\":1,\"build\":21100}"
            }
        ],
        "lastTime": 1535379107049
    }
}
```

关于**extInfo**字段：
```
{
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
```

已知**messageObject**:

序号 | 名称 | 说明
---- | --- | ----
1 | faipaiText | 翻牌
2 | text | 文本消息    
3 | image | 图片分享
4 | idolFlip | 提问信息翻牌，仅直接显示成员回复
5 | live | 视频直播
6 | diantai | 电台直播
