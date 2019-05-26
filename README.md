# SNH48G-API:heart:

收集整理关于 SNH48 Group 的 API ，包括口袋 48 ，官网，微博等

* [2019-04-15 20:06:05] 今天得知丝芭重做了 APP ，所以 APP 的接口凉了， 而且打卡也没鸡腿了。
* [2019-05-26 16:24:38] 票务信息接口更新，可查询全团票务

### 相关说明

API 中**输入参数**使用变量名占位

```
{name}
```

相关隐私信息中**数字**按位取 1：1990 -> 1111；**字符串**统一用'XXXXXX'替换。

### room-id

获取房间消息等请求涉及到的必输字段，详情见 [room-id](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/room-id.md) 。

### APIs List

分类按**添加时间**排序

#### 口袋 48（pocket48）

| 序号 | 功能 | 更新时间 | 备注 |
| ---- | :--- | :-------- | :-- |
| 1 | [登录](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/login.md) | 2018-08-26 |  |
| 2 | [公演直播](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/group-live.md) | 2018-08-26 |  |
| 3 | [成员直播](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/member-live.md) | 2018-08-27 |  |
| 4 | [成员直播详情](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/live-detail.md) | 2018-08-27|  |
| 5 | [成员房间消息](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/member-room-message.md) | 2018-08-28|  |
| 6 | [打卡](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/check-in.md) | 2018-09-01|  |
| 7 | [登录用户信息](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/user-info.md) | 2018-09-29|  |
| 8 | [成员房间基本信息](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/room-info.md) | 2018-10-09| room-id |
| 9 | [缓存数据](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/overview.md) | 2018-10-09| 成员信息 |

#### 官网（OS - Official Site）

| 序号 | 功能 | 更新时间 |
| ---- | :--- | :-------- |
| 1 | [条件查询成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/members.md) | 2018-08-26 |
| 2 | [SNH48 成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/SNH48-members.md) | 2018-08-26 |
| 3 | [BEJ48 成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/BEJ48-members.md) | 2018-08-26 |
| 4 | [GNZ48 成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/GNZ48-members.md) | 2018-08-26 |
| 5 | [SHY48 成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/SHY48-members.md) | 2018-08-26 |
| 6 | [CKG48 成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/CKG48-members.md) | 2018-08-26 |
| 7 | [票务信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/tickets-info.md) | 2019-05-26 |
| 8 | [EP 信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/ep.md) | 2018-08-27 |
| 9 | [活动信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/event.md) | 2018-08-27 |

#### 备注

1. 已知 **SNH48 成员信息**中所有成员基本信息不包含 Ft 成员

#### JSON

可通过 JSON 文件夹下的相关 json 文件实现快速配置请求相关参数

