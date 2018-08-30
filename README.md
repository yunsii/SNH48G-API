# SNH48G-API
收集整理关于SNH48Group的API，包括口袋48，官网，微博等:heart:

## 相关说明

API中**输入参数**使用变量名占位：
```
{name}
```
相关隐私信息中**数字**按位取1：1990 -> 1111；**字符串**统一用'xxxxxx'替换。

添加API测试方法[request_test.py](https://github.com/theprimone/SNH48G-API/blob/master/request_test.py)，基于自写简单工具包[theprimone.py](https://github.com/theprimone/theprimone/blob/master/theprimone.py)

## room-id

获取房间消息等请求涉及到的必输字段，详情见[room-id](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/room-id.md)。

## APIs List:

分类按**添加时间**排序

### 口袋48（pocket48）
1. [登录API](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/login.md)
2. [公演直播API](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/group-live.md)
3. [成员直播API](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/member-live.md)
4. [直播详情API](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/live-detail.md)
5. [成员房间消息API](https://github.com/theprimone/SNH48G-API/blob/master/pocket48/member-room-message.md)

### 官网（OS - Official Site）
1. [条件查询成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/members.md)
2. [SNH48成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/SNH48-members.md)
3. [BEJ48成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/BEJ48-members.md)
4. [GNZ48成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/GNZ48-members.md)
5. [SHY48成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/SHY48-members.md)
6. [CKG48成员信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/CKG48-members.md)
7. [票务信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/tickets-info.md)
8. [EP信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/ep.md)
9. [活动信息](https://github.com/theprimone/SNH48G-API/blob/master/OS/event.md)

### 备注
1. 已知**SNH48成员信息**中所有成员基本信息不包含Ft成员

