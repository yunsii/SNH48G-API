from util.theprimone import get_response, dict2format_string


def api_test():
    """
    POST请求
    :return:
    """
    url = 'https://plive.48.cn/livesystem/api/live/v1/memberLivePage'

    header = {
        'version': '5.0.1',
        'os': 'android',
        'Content-Type': 'application/json;charset=utf-8',
    }
    form = {
        # "lastTime": 0,
        # "groupId": 0,
        # "type": 0,
        # "memberId": 0,
        # "giftUpdTime": 1533711602000,
        # "limit": 20
    }
    res = get_response(is_json=True, url=url, method="post", headers=header, json=form)
    # res = requests.post(
    #     url,
    #     data=json.dumps(form),
    #     headers=header,
    #     # verify=False
    # ).json()
    return res


if __name__ == "__main__":
    # print(dict2format_string(
    #     get_response(
    #         is_json=True, url="http://www.snh48.com/mobile/json/event.json", method="get"
    #     )
    # ))

    print(dict2format_string(api_test()))

