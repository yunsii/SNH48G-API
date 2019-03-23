# 成员信息

GET

http://h5.snh48.com/resource/jsonp/members.php

## 说明

根据条件查询团体成员基本信息


## 请求头

```python
{
    # 无
}
```

## 查询参数(必填)

```python
{
    "gid": 10  # http://h5.snh48.com/resource/jsonp/members.php?gid=10
}
```

## 查询参数说明

名称 | 说明 | 必填 | 备注
------- | ------- | ----- | ----
gid | group id | Y | 10-SNH/ 11-BEJ/ 12-GNZ/ 13-SHY48/ 14-CKG48

### 小提示

响应为 **jsonp**格式

当gid为乱码，例如

```python
{
    "gid": "xx"
}
```

返回全团成员信息。

另，已知熊心瑶有sid为30031和50015两条信息。

## 响应

### 成功

```python
{
    "total": "126",
    "rows": [
        {
            "sid": "10001",
            "gid": "10",
            "gname": "SNH",
            "sname": "陈观慧",
            "fname": "陈 观慧",
            "pinyin": "Chen GuanHui",
            "abbr": "CGH",
            "tid": "101",
            "tname": "SII",
            "pid": "1001",
            "pname": "SNH48 一期生",
            "nickname": "小艾",
            "company": "上海丝芭文化传媒集团有限公司",
            "join_day": "2012-10-14",
            "height": "161",
            "birth_day": "08.28",
            "star_sign_12": "处女座",
            "star_sign_48": "系统化处女座，系统化的一周，8.26-9.2",
            "birth_place": "中国 广东 ",
            "speciality": "唱歌、跳舞、画画",
            "hobby": "爵士鼓、跳舞",
            "experience": "2012.10.14 加入SNH48一期生<br>2013.04.17 一期生审查通过认可为SNH48正式一期生<br>2013.11.11 加入SNH48TeamS队（TeamSII）<br>2014.07.26 SNH48第一届总决选第十名<br>2015.07.25 SNH48第二届总决选第二十二名<br>2016.07.30 SNH48第三届总决选第四十七名<br>2017.07.29 SNH48 GROUP第四届总决选第六十一名",
            "catch_phrase": "我对你“艾艾艾”不完。。。。",
            "weibo_uid": "3050708243",
            "weibo_verifier": "655ac839",
            "blood_type": "A",
            "tieba_kw": "陈观慧",
            "status": "99",
            "tcolor": "91cdeb",
            "gcolor": "8ed2f5"
        },
        {
            "sid": "10002",
            "gid": "10",
            "gname": "SNH",
            "sname": "陈思",
            "fname": "陈 思",
            "pinyin": "Chen Si",
            "abbr": "CS",
            "tid": "101",
            "tname": "SII",
            "pid": "1001",
            "pname": "SNH48 一期生",
            "nickname": "教练",
            "company": "上海丝芭文化传媒集团有限公司",
            "join_day": "2012-10-14",
            "height": "163",
            "birth_day": "09.14",
            "star_sign_12": "处女座",
            "star_sign_48": "真我处女座，真我的一周，9.11-9.18",
            "birth_place": "中国 湖南 ",
            "speciality": "双节棍、散打、配音",
            "hobby": "看动漫、做美食、和朋友一起逛街",
            "experience": "2012.10.14 加入SNH48一期生<br>2013.04.17 一期生审查通过认可为SNH48正式一期生<br>2013.11.11 加入SNH48TeamS队（TeamSII）<br>2014.07.26 SNH48第一届总决选第九名<br>2015.07.25 SNH48第二届总决选第二十四名<br>2016.07.30 SNH48第三届总决选第三十八名",
            "catch_phrase": "教练教练甜过初恋，初恋初恋不如教练",
            "weibo_uid": "3050742117",
            "weibo_verifier": "655ac839",
            "blood_type": "O",
            "tieba_kw": "陈思",
            "status": "99",
            "tcolor": "91cdeb",
            "gcolor": "8ed2f5"
        }
        # 省略...
    ]
}
```

#### gid为乱码时

```python
{
    "total": "409",
    "rows": [
        {
            "sid": "10001",
            "gid": "10",
            "gname": "SNH",
            "sname": "陈观慧",
            "fname": "陈 观慧",
            "pinyin": "Chen GuanHui",
            "abbr": "CGH",
            "tid": "101",
            "tname": "SII",
            "pid": "1001",
            "pname": "SNH48 一期生",
            "nickname": "小艾",
            "company": "上海丝芭文化传媒集团有限公司",
            "join_day": "2012-10-14",
            "height": "161",
            "birth_day": "08.28",
            "star_sign_12": "处女座",
            "star_sign_48": "系统化处女座，系统化的一周，8.26-9.2",
            "birth_place": "中国 广东 ",
            "speciality": "唱歌、跳舞、画画",
            "hobby": "爵士鼓、跳舞",
            "experience": "2012.10.14 加入SNH48一期生<br>2013.04.17 一期生审查通过认可为SNH48正式一期生<br>2013.11.11 加入SNH48TeamS队（TeamSII）<br>2014.07.26 SNH48第一届总决选第十名<br>2015.07.25 SNH48第二届总决选第二十二名<br>2016.07.30 SNH48第三届总决选第四十七名<br>2017.07.29 SNH48 GROUP第四届总决选第六十一名",
            "catch_phrase": "我对你“艾艾艾”不完。。。。",
            "weibo_uid": "3050708243",
            "weibo_verifier": "655ac839",
            "blood_type": "A",
            "tieba_kw": "陈观慧",
            "status": "99",
            "tcolor": "91cdeb",
            "gcolor": "8ed2f5"
        },
        {
            "sid": "10002",
            "gid": "10",
            "gname": "SNH",
            "sname": "陈思",
            "fname": "陈 思",
            "pinyin": "Chen Si",
            "abbr": "CS",
            "tid": "101",
            "tname": "SII",
            "pid": "1001",
            "pname": "SNH48 一期生",
            "nickname": "教练",
            "company": "上海丝芭文化传媒集团有限公司",
            "join_day": "2012-10-14",
            "height": "163",
            "birth_day": "09.14",
            "star_sign_12": "处女座",
            "star_sign_48": "真我处女座，真我的一周，9.11-9.18",
            "birth_place": "中国 湖南 ",
            "speciality": "双节棍、散打、配音",
            "hobby": "看动漫、做美食、和朋友一起逛街",
            "experience": "2012.10.14 加入SNH48一期生<br>2013.04.17 一期生审查通过认可为SNH48正式一期生<br>2013.11.11 加入SNH48TeamS队（TeamSII）<br>2014.07.26 SNH48第一届总决选第九名<br>2015.07.25 SNH48第二届总决选第二十四名<br>2016.07.30 SNH48第三届总决选第三十八名",
            "catch_phrase": "教练教练甜过初恋，初恋初恋不如教练",
            "weibo_uid": "3050742117",
            "weibo_verifier": "655ac839",
            "blood_type": "O",
            "tieba_kw": "陈思",
            "status": "99",
            "tcolor": "91cdeb",
            "gcolor": "8ed2f5"
        }
        # 省略...
    ]
}
```
