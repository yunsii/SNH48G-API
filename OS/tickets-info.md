# 票务信息

GET

http://www.snh48.com/ticketsinfo.php

## 说明

根据条件查询票务信息


## 请求头

```python
{
    # 无
}
```

## 查询参数(必填)

```python
{
    "act": "recent",  # http://www.snh48.com/ticketsinfo.php?act=recent
    "date": "2018-8"
}
```

## 查询参数说明：

名称 | 说明 | 必填 | 备注
---- | --- | ---- | -----
act  |     |  Y  |      | 
date | 起始时间 | N | 不指定date，返回所有票务信息

## 响应：

### 成功：

```python
[
    {
        "id": "1422",
        "title": "《双面偶像》首演",
        "addtime": "2018-09-02 19:00",
        "theme": "新公演首演</br>限定实名认证检票，网络直播",
        "auction_url": "https://shop.48.cn/pai/item/3952",
        "acstatus": "0",
        "vip_url": "https://shop.48.cn/tickets/item/2381?seat_type=2",
        "vstatus": "0",
        "common_url": "https://shop.48.cn/tickets/item/2381?seat_type=3",
        "cstatus": "1",
        "stand_url": "https://shop.48.cn/tickets/item/2381?seat_type=4",
        "sstatus": "0",
        "type": "99",
        "special": "新公演首演</br>限定实名认证检票，网络直播",
        "tickets_price": "超级VIP座（168元+积分竞价）、站席80元 普通坐席80元 VIP坐席168元（<a href=\"http://www.snh48.com/ticket_faq.html\">丝瓜享受优惠票价</a>）",
        "teamname": "Ft队",
        "pretime": "1535886000",
        "team_id": "21",
        "oversea": "2",
        "style": 1
    },
    {
        "id": "1421",
        "title": "《双面偶像》首演",
        "addtime": "2018-09-01 19:00",
        "theme": "新公演首演，随机抽选场</br>限定实名认证检票，网络直播",
        "auction_url": "https://shop.48.cn/pai/item/3940",
        "acstatus": "0",
        "vip_url": "https://shop.48.cn/tickets/item/2377?seat_type=2",
        "vstatus": "0",
        "common_url": "https://shop.48.cn/tickets/item/2377?seat_type=3",
        "cstatus": "0",
        "stand_url": "https://shop.48.cn/tickets/item/2377?seat_type=4",
        "sstatus": "0",
        "type": "-1",
        "special": "新公演首演，随机抽选场</br>限定实名认证检票，网络直播",
        "tickets_price": "超级VIP座（168元现金竞价）、站席80元 普通坐席80元 VIP坐席168元（<a href=\"http://www.snh48.com/ticket_faq.html\">丝瓜享受优惠票价</a>）",
        "teamname": "Ft队",
        "pretime": "1535799600",
        "team_id": "21",
        "oversea": "1",
        "style": 1
    }
    # 省略...
]
```
