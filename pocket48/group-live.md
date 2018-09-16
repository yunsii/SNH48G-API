# 公演直播

API:

https://plive.48.cn/livesystem/api/live/v1/openLivePage

## 请求头：
```python
{
    "version": "5.0.1",
    "os": "android",
    "Content-Type": "application/json;charset=utf-8",
}
```

## 表单数据：
```python
{
    # "isReview": 1,
    # "groupId": 0,
    # "userId": 0,
    # "lastGroupId": 0,
    # "lastTime": 0,
    # "type": 0,
    # "giftUpdTime": 1533711602000,
    # "limit": 20
}
```

## 已知表单参数说明：
名称 | 类型 | 说明 | 必填 | 默认值 | 备注
------- | -------- | ------- | ---- | ----- | ----
isReview | int | 是否回放 | N | 0 | 0-No/ 1-Yes
groupId | int | 团体id | N | 0 | 0-全团/ 10-SNH/ 11-BEJ/ 12-GNZ/ 13-SHY48/ 14-CKG48
userId | int | 用户id | N |  | 
lastGroupId | int |  | N |  | 
lastTime | int |  | N |  | 
type | int |  | N |  | 
giftUpdTime | int | 礼物更新时间 | N |  | 
limit | int |  | N |  | 配置前后都返回全部直播信息

## 提示：
经测试，即使表单为空也要发送，否则返回报错信息：
```python
{
    "status": 400,
    "message": "Required request body is missing: public com.google.gson.JsonObject \
        com.snh.livesystem.restapi.controller.LiveController.openLivePage( \
        com.snh.livesystem.entity.request.LivePageReq,org.springframework.validation.BindingResult)"
}
```

## 响应：

### 成功：

#### isReview : 0
```python
{
    "status": 200,
    "message": "请求成功",
    "content": {
        "liveList": [
            {
                "liveId": "5b72ae0f0cf2e0b32c118c8f",
                "title": "《UNIVERSE》剧场公演",
                "subTitle": "顼凘炀生日公演",
                "picPath": "/mediasource/live/15342423193598Jkxt9fq74.jpg",
                "isOpen": true,
                "startTime": 1535262300000,
                "count": {
                    "praiseCount": 307,
                    "commentCount": 11,
                    "memberCommentCount": 0,
                    "shareCount": 12,
                    "quoteCount": 0
                },
                "isLike": false,
                "groupId": 11
            },
            {
                "liveId": "5b796a760cf296d2ab2d0bfb",
                "title": "《少女进化论》剧场公演",
                "subTitle": "关思雨生日公演",
                "picPath": "/mediasource/live/1534683766385iMZfpIe7SO.jpg",
                "isOpen": true,
                "startTime": 1535262300000,
                "count": {
                    "praiseCount": 199,
                    "commentCount": 5,
                    "memberCommentCount": 0,
                    "shareCount": 4,
                    "quoteCount": 0
                },
                "isLike": false,
                "groupId": 13
            }
            # 省略...
        ]
    }
}
```

#### isReview : 1  # 回放
```python
{
    "status": 200,
    "message": "请求成功",
    "content": {
        "liveList": [
            {
                "liveId": "5b72a1930cf2e0b32c118c85",
                "title": "吴羽霏生日会",
                "subTitle": "吴羽霏生日冷餐会",
                "picPath": "/mediasource/live/15342391229148rwYyI4z02.jpg",
                "isOpen": false,
                "startTime": 1535256000000,
                "count": {
                    "praiseCount": 286,
                    "commentCount": 82,
                    "memberCommentCount": 0,
                    "shareCount": 8,
                    "quoteCount": 0
                },
                "isLike": false,
                "groupId": 12
            },
            {
                "liveId": "5b72ae590cf2e0b32c118c90",
                "title": "顼凘炀生日会",
                "subTitle": "参加成员：",
                "picPath": "/mediasource/live/1534242393567IwM2Vk0d1g.jpg",
                "isOpen": false,
                "startTime": 1535254200000,
                "count": {
                    "praiseCount": 318,
                    "commentCount": 50,
                    "memberCommentCount": 0,
                    "shareCount": 15,
                    "quoteCount": 0
                },
                "isLike": false,
                "groupId": 11
            }
            # 省略...
        ]
    }
}
```
