# 直播详情

API:

https://plive.48.cn/livesystem/api/live/v1/getLiveOne

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
    "type": 1,
    # "userId": 0,
    "liveId": "5b83e2b00cf2234479b4cbc9"
}
```

## 已知表单参数说明：
名称 | 类型 | 说明 | 必填 | 默认值 | 备注
------- | -------- | ------- | ---- | ----- | ----
type | int | 是否回放 | Y | 0 | 1-视频/ 2-电台
userId | int |  | N | 0 | 
liveId | str | 直播id | Y |  | 

## 提示：
经测试，必填信息不填返回信息：
```python
{
    "status": 20018,
    "message": "直播内容取得失败"
}
```

## 响应：

### 成功：

####
```python
{
    "status": 200,
    "message": "请求成功",
    "content": {
        "title": "赵佳蕊的直播间",
        "subTitle": "小蕊在线摸狗",
        "picPath": "/mediasource/live/1535276698080RR8h7F2Sfw.jpg",
        "streamPath": "http://pl.live.weibo.com/alicdn/089ab058f2b92fb6504e842d9df9d601_wb480.flv",
        "streamPathLd": "",
        "streamPathHd": "",
        "startTime": 1535369904492,
        "isOpen": false,
        "isLike": false,
        "roomId": "6486104",
        "liveType": 1,
        "openLiveType": 0,
        "systemMessage": "系统公告:欢迎来到$1的直播间,请大家文明观看，注意弹幕礼仪，不要进行任何骚扰成员的行为！",
        "memberId": 460005,
        "isReview": false,
        "needForward": true,
        "udpKey": "",
        "loopTime": 5000,
        "canVote": false,
        "voteMemberId": 40017,
        "number": 2889,
        "maxChatCount": 20,
        "isTop": false,
        "isSpecial": false,
        "specialUrl": "",
        "keepSeconds": 0,
        "lrcPath": "/mediasource/live/lrc/5b83e2b00cf2234479b4cbc9.lrc",
        "picLoopTime": 0,
        "userMoney": 0,
        "textMoney": 10,
        "textMelee": 10,
        "screenMode": 0,
        "spAchievementPath": "",
        "topList": [],
        "giftInfo": [
            {
                "giftId": "5a72d852922a84e222f41da0",
                "giftName": "生日蛋糕",
                "giftPic": "/mediasource/gift/1517471186334pA4Y8A3l39.png",
                "giftMoney": 2880,
                "giftMelee": 2880,
                "clickFlg": 0,
                "specialFlg": 1,
                "time": 63,
                "looptimes": 1,
                "fadeFlg": 0,
                "swcDmFlg": false
            },
            {
                "giftId": "57b3cad50cf22621dc6cbbe6",
                "giftName": "巧克力",
                "giftPic": "/mediasource/gift/1ce972c0-1b09-489d-9e10-a4a887237160.png",
                "giftMoney": 10,
                "giftMelee": 10,
                "clickFlg": 1,
                "specialFlg": 0,
                "time": 0,
                "looptimes": 0,
                "fadeFlg": 0,
                "swcDmFlg": false
            }
            # 省略...
        ],
        "emoticonInfo": [],
        "swcGift": [
            {
                "giftId": "5ad98f150cf2bf2ffcd84b12",
                "giftName": "超级弹幕",
                "giftPic": "/mediasource/gift/1524207375602vWy5m52aje.png",
                "giftMoney": 50,
                "giftMelee": 50,
                "clickFlg": 0,
                "specialFlg": 0,
                "time": 0,
                "looptimes": 0,
                "fadeFlg": 0,
                "swcDmFlg": true
            },
            {
                "giftId": "5ad99f5b0cf2bf2ffcd84b16",
                "giftName": "SNH48 Family",
                "giftPic": "/mediasource/gift/1524211545361ZI0xxU0T52.png",
                "giftMoney": 88,
                "giftMelee": 88,
                "clickFlg": 0,
                "specialFlg": 1,
                "time": 63,
                "looptimes": 1,
                "fadeFlg": 0,
                "swcDmFlg": false
            }
        ]
    }
}
```
