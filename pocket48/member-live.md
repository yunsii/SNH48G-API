# 成员直播

## 接口

POST

https://plive.48.cn/livesystem/api/live/v1/memberLivePage

### 请求头

```python
{
    "version": "5.0.1",
    "os": "android",
    "Content-Type": "application/json;charset=utf-8"
}
```

### 表单

```python
{
    # "lastTime": 0,
    # "groupId": 0,
    # "type": 0,
    # "memberId": 0,
    # "giftUpdTime": 1533711602000,
    # "limit": 20
}
```

### 已知表单参数说明（根据[group-live](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/group-live.md)推测，未验证）

名称 | 类型 | 说明 | 必填 | 默认值 | 备注
------- | -------- | ------- | ---- | ----- | ----
lastTime | int | 该时间点前直播 | N | 0 | 13位时间戳，0为当前
groupId | int | 团体id | N | 0 | 0-全团/ 10-SNH/ 11-BEJ/ 12-GNZ/ 13-SHY48/ 14-CKG48
type | int |  | N |  | 
memberId | int |  | N |  | 
giftUpdTime | int | 礼物更新时间 | N |  | 
limit | int |  | N |  | 配置前后都返回全部直播信息

### 提示

经测试，即使表单为空也要发送，否则返回报错信息：

```python
{
    "status": 400,
    "message": "Required request body is missing: public com.google.gson.JsonObject \
        com.snh.livesystem.restapi.controller.LiveController.openLivePage( \
        com.snh.livesystem.entity.request.LivePageReq,org.springframework.validation.BindingResult)"
}
```

### 响应

#### 成功

```python
{
    "status": 200,
    "message": "请求成功",
    "content": {
        "liveList": [
            {
                "liveId": "5b83e2b00cf2234479b4cbc9",
                "title": "赵佳蕊的直播间",
                "subTitle": "小蕊在线摸狗",
                "picPath": "/mediasource/live/1535276698080RR8h7F2Sfw.jpg",
                "startTime": 1535369904492,
                "memberId": 460005,
                "liveType": 1,
                "picLoopTime": 0,
                "lrcPath": "/mediasource/live/lrc/5b83e2b00cf2234479b4cbc9.lrc",
                "streamPath": "http://pl.live.weibo.com/alicdn/089ab058f2b92fb6504e842d9df9d601_wb480.flv",
                "screenMode": 0,
                "roomId": "6486104",
                "bwqaVersion": 0
            },
            {
                "liveId": "5b83e1ff0cf26dbbba13ed0d",
                "title": "左欣的直播间",
                "subTitle": "唠嗑",
                "picPath": "/mediasource/live/153536802451312eV5L47fP.png",
                "startTime": 1535369727431,
                "memberId": 614742,
                "liveType": 1,
                "picLoopTime": 0,
                "lrcPath": "/mediasource/live/lrc/5b83e1ff0cf26dbbba13ed0d.lrc",
                "streamPath": "http://2519.liveplay.myqcloud.com/live/2519_3633775.flv",
                "screenMode": 0,
                "roomId": "19836397",
                "bwqaVersion": 0
            }
            # 省略...
        ],
        "reviewList": [
            {
                "liveId": "5b83dd950cf2f04fd1e1292c",
                "title": "许杨玉琢的电台（回放生成中）",
                "subTitle": "十分钟❤️怕之后没时间",
                "picPath": "/mediasource/live/1535368526610mmE0ln6B4F.jpg,/mediasource/live/1534510915382nH9ziRD74t.jpg",
                "startTime": 1535368597002,
                "memberId": 5566,
                "liveType": 2,
                "picLoopTime": 30000,
                "lrcPath": "/mediasource/live/lrc/5b83dd950cf2f04fd1e1292c.lrc",
                "streamPath": "https://mp4.48.cn/live/69d2e70c-b7c8-4a73-83e3-63c12f160c6d.mp4",
                "screenMode": 0,
                "roomId": "3868298",
                "bwqaVersion": 0
            },
            {
                "liveId": "5b83d9420cf2f04fd1e12929",
                "title": "林思意的直播间（回放生成中）",
                "subTitle": "“死亡”直播之——我妈在睡觉我在吃火锅",
                "picPath": "/mediasource/live/1532794329263914Txe5137.jpg",
                "startTime": 1535367490181,
                "memberId": 24,
                "liveType": 1,
                "picLoopTime": 0,
                "lrcPath": "/mediasource/live/lrc/5b83d9420cf2f04fd1e12929.lrc",
                "streamPath": "https://mp4.48.cn/live/1d851246-5c19-4ca3-8fc1-2ac3181b8e0c.mp4",
                "screenMode": 0,
                "roomId": "3870020",
                "bwqaVersion": 0
            }
            # 省略...
        ],
        "giftUpdTime": 1533711602000,
        "giftUpdUrl": [
            "/mediasource/gift/5b2339720cf26dbef1642888.zip",
            "/mediasource/gift/5aa907230cf2a0da4ea3271e.zip"
            # 省略...
        ],
        "hasReviewUids": [
            327587,
            399662
            # 省略...
        ]
    }
}
```
