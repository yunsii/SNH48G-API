# 票务信息

## SNH48 Group 票务信息

GET

https://m.48.cn/Home/IndexTickets?brand_id=-1&team_type=-1&date_type=0


### 请求头

无

### 查询参数

```python
{
    "brand_id": "-1",  # 1 / SNH48, 2 / BEJ48, 3 / GNZ-48, 4 / SHY48, 5 / CKG48
    "team_type": "-1",  # [S, N, H, X, XII, 联合, Ft], [B, E, 联合, J], [G, N, 联合, Z, 预备生], [SIII, HIII, 联合], [C, K, 联合] 按位取索引
    "date_type": "0",  # 0 / 本周和下周, 1 / 本周, 2 / 下周
    "r": "0.1934004182578133",  # 未知参数
}
```

### 响应

```python
[
    {
        "tickets_id": 3065,
        "theatre_id": 6,
        "brand_id": 2,
        "is_on_sale": false,
        "start_playdate": "\/Date(1559473200000)\/",
        "tickets_name": "星梦剧院6月2日B队公演",
        "team_type": 0,
        "team_type_brand_id": 2,
        "merchandise_type": 0,
        "tickets_sales": [
            {
                "seat_type": 1,
                "amount": 0,
                "price": 168.0000,
                "rank_integral": -1
            },
            {
                "seat_type": 2,
                "amount": 0,
                "price": 168.0000,
                "rank_integral": -1
            },
            {
                "seat_type": 3,
                "amount": 1,
                "price": 80.0000,
                "rank_integral": -1
            },
            {
                "seat_type": 4,
                "amount": 1,
                "price": 80.0000,
                "rank_integral": -1
            }
        ],
        "theatre_id_name": "北京"
    },
    {
        "tickets_id": 3064,
        "theatre_id": 6,
        "brand_id": 2,
        "is_on_sale": false,
        "start_playdate": "\/Date(1559455200000)\/",
        "tickets_name": "星梦剧院6月2日E队公演",
        "team_type": 1,
        "team_type_brand_id": 2,
        "merchandise_type": 0,
        "tickets_sales": [
            {
                "seat_type": 1,
                "amount": 0,
                "price": 168.0000,
                "rank_integral": -1
            },
            {
                "seat_type": 2,
                "amount": 0,
                "price": 168.0000,
                "rank_integral": -1
            },
            {
                "seat_type": 3,
                "amount": 1,
                "price": 80.0000,
                "rank_integral": -1
            },
            {
                "seat_type": 4,
                "amount": 1,
                "price": 80.0000,
                "rank_integral": -1
            }
        ],
        "theatre_id_name": "北京"
    },
    # 省略...
]
```


## SNH48 票务信息

GET

http://www.snh48.com/ticketsinfo.php


### 请求头

无

### 查询参数

```python
{
    "act": "recent",  # http://www.snh48.com/ticketsinfo.php?act=recent
    "date": "2018-8"
}
```

### 查询参数说明

名称 | 说明 | 必填 | 备注
---- | --- | ---- | -----
act  |     |  Y  |      | 
date | 起始时间 | N | 不指定date，返回所有票务信息

### 响应

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
    },
    # 省略...
]
```
