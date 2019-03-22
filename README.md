# SNH48G-API:heart:

收集整理关于SNH48Group的API，包括口袋48，官网，微博等

## 相关说明

API中**输入参数**使用变量名占位

```
{name}
```

相关隐私信息中**数字**按位取1：1990 -> 1111；**字符串**统一用'XXXXXX'替换。

## room-id

获取房间消息等请求涉及到的必输字段，详情见[room-id](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/room-id.md)。

## APIs List

分类按**添加时间**排序

### 口袋48（pocket48）

| 序号 | 功能 | 更新时间 | 备注 |
| ---- | :--- | :-------- | :-- |
| 1 | [登录API](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/login.md) | 2018-08-26 |  |
| 2 | [公演直播API](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/group-live.md) | 2018-08-26 |  |
| 3 | [成员直播API](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/member-live.md) | 2018-08-27 |  |
| 4 | [成员直播详情API](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/live-detail.md) | 2018-08-27|  |
| 5 | [成员房间消息API](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/member-room-message.md) | 2018-08-28|  |
| 6 | [打卡API](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/check-in.md) | 2018-09-01|  |
| 7 | [登录用户信息API](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/user-info.md) | 2018-09-29|  |
| 8 | [成员房间基本信息API](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/room-info.md) | 2018-10-09| room-id |
| 9 | [缓存数据API](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/overview.md) | 2018-10-09| 成员信息 |

### 官网（OS - Official Site）

| 序号 | 功能 | 更新时间 |
| ---- | :--- | :-------- |
| 1 | [条件查询成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/members.md) | 2018-08-26 |
| 2 | [SNH48成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/SNH48-members.md) | 2018-08-26 |
| 3 | [BEJ48成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/BEJ48-members.md) | 2018-08-26 |
| 4 | [GNZ48成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/GNZ48-members.md) | 2018-08-26 |
| 5 | [SHY48成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/SHY48-members.md) | 2018-08-26 |
| 6 | [CKG48成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/CKG48-members.md) | 2018-08-26 |
| 7 | [票务信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/tickets-info.md) | 2018-08-27|
| 8 | [EP信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/ep.md) | 2018-08-27|
| 9 | [活动信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/event.md) | 2018-08-27|

### 备注

1. 已知**SNH48成员信息**中所有成员基本信息不包含Ft成员

### JSON

可通过JSON文件夹下的相关json文件实现快速配置请求相关参数

