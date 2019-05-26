# 票务信息

经研究，SNH48 和 GNZ48 后台应该是同一套系统，接口有路由和响应结果上的差别。而 BEJ48 是另一套系统，从接口的方式和响应字段都有明显的差别。CKG48 后台又是一套系统。

## SNH48 Group 票务信息（精简版）

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

http://www.snh48.com/ticketsinfo.php?act=recent&date=2018-8

### 请求头

无

### 查询参数

```python
{
    "act": "recent",
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

## BEJ48 票务信息

POST

http://www.bej48.com/index/ticket/category_data.html

### 请求头

无

### 表单参数

```python
{
    "time": "null",
    "team": "null"  # null 全部信息
}
```

参数 `time` 的格式形如 `2019-05`

### 响应

```python
[
    {
        "id": 692,
        "name": "TeamB《十八个闪耀瞬间-绝密代码》剧场公演",
        "time": "2019-06-02 19:00:00",
        "price": "超级VIP座（168元+积分竞价）、VIP座席168元、普通座席80元、 站席80元（BEJ48丝瓜限时享受优惠票价）",
        "description": "《十八个闪耀瞬间-绝密代码》剧场公演 程戈+曲美霖拉票公演 限定实名认证检票 本场公演将进行网络直播",
        "category_id": "34",
        "create_time": 1558424912,
        "update_time": 1558424912,
        "status": 1,
        "closing_date": "2019年05月28日",
        "closing_date1": 1559029712,
        "auction_is_on_sale": 0,
        "auction_url": "http://shop.48.cn/pai/Item/5438",
        "vip_is_on_sale": 0,
        "vip_url": "https://shop.48.cn/Tickets/Item/3065?seat_type=2",
        "common_is_on_sale": 1,
        "common_url": "https://shop.48.cn/Tickets/Item/3065?seat_type=3",
        "stand_is_on_sale": 1,
        "stand_url": "https://shop.48.cn/Tickets/Item/3065?seat_type=4"
    },
    {
        "id": 691,
        "name": "TeamE《UNIVERSE》剧场公演",
        "time": "2019-06-02 14:00:00",
        "price": "超级VIP座（168元+积分竞价）、VIP座席168元、普通座席80元、 站席80元（BEJ48丝瓜限时享受优惠票价）",
        "description": "《UNIVERSE》剧场公演 熊鑫生日+拉票公演 限定实名认证检票 本场公演将进行网络直播",
        "category_id": "35",
        "create_time": 1558424867,
        "update_time": 1558424867,
        "status": 1,
        "closing_date": "2019年05月28日",
        "closing_date1": 1559029667,
        "auction_is_on_sale": 0,
        "auction_url": "http://shop.48.cn/pai/Item/5437",
        "vip_is_on_sale": 0,
        "vip_url": "https://shop.48.cn/Tickets/Item/3064?seat_type=2",
        "common_is_on_sale": 1,
        "common_url": "https://shop.48.cn/Tickets/Item/3064?seat_type=3",
        "stand_is_on_sale": 1,
        "stand_url": "https://shop.48.cn/Tickets/Item/3064?seat_type=4"
    },
    # 省略...
]
```

## GNZ48 票务信息

GET

http://www.gnz48.com/ticket/ticketsinfo.php?act=recent

### 请求头

无

### 查询参数

```python
{
    "act": "recent",
    "date": "2019-5"
}
```

### 查询参数说明

名称 | 说明 | 必填 | 备注
---- | --- | ---- | -----
act  |     |  Y  |      | 
date | 起始时间 | N | [推测]不指定 date ，返回最近 40 场票务信息

### 响应

```python
[
    {
        "id": "694",
        "title": "星梦剧院6月2日S队广州巡演",
        "addtime": "2019-06-02 19:00",
        "theme": "星梦剧院6月2日S队广州巡演",
        "auction_url": "https://shop.48.cn/pai/item/5433",
        "acstatus": "0",
        "vip_url": "https://shop.48.cn/tickets/item/3060?seat_type=2",
        "vstatus": "0",
        "common_url": "https://shop.48.cn/tickets/item/3060?seat_type=3",
        "cstatus": "0",
        "stand_url": "https://shop.48.cn/tickets/item/3060?seat_type=4",
        "sstatus": "0",
        "type": "99",
        "special": "SNH48 Team SII《重生计划》广州巡演，限定实名认证检票，本场公演将进行网络直播",
        "tickets_price": "超级VIP座（168元+积分竞价）、站席80元、普通坐席80元、VIP坐席168元（丝瓜享受优惠票价）",
        "teamname": null,
        "pretime": "1559473200",
        "team_id": "26",
        "oversea": "1",
        "style": 1
    },
    {
        "id": "693",
        "title": "星梦剧院6月2日Z队《三角函数》方琪，杨可璐拉票公演",
        "addtime": "2019-06-02 14:00",
        "theme": "星梦剧院6月2日Z队《三角函数》方琪，杨可璐拉票公演",
        "auction_url": "https://shop.48.cn/pai/item/5432",
        "acstatus": "0",
        "vip_url": "https://shop.48.cn/tickets/item/3059?seat_type=2",
        "vstatus": "0",
        "common_url": "https://shop.48.cn/tickets/item/3059?seat_type=3",
        "cstatus": "1",
        "stand_url": "https://shop.48.cn/tickets/item/3059?seat_type=4",
        "sstatus": "1",
        "type": "99",
        "special": "《三角函数》方琪，杨可璐拉票公演，限定实名认证检票，本场公演将进行网络直播",
        "tickets_price": "超级VIP座（168元+积分竞价）、站席80元、普通坐席80元、VIP坐席168元（丝瓜享受优惠票价）",
        "teamname": null,
        "pretime": "1559455200",
        "team_id": "28",
        "oversea": "1",
        "style": 1
    },
    # 省略...
]
```
