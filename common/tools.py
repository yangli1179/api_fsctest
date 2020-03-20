# -*- coding: utf-8 -*-
"""

=================================
Author: yangli
Created on: 2020/3/12

E-mail:1179384105@qq.com

=================================


"""

import random
from common.http_request import HTTPRequest


def random_ip():
    ip = "{}.{}.{}.{}".format(random.randint(0, 255), random.randint(0, 255),
                              random.randint(0, 255), random.randint(0, 255))
    return ip


def get_token(phone, pwd):
    request = HTTPRequest()
    method = "post"
    url = "https://fsc-test.manshang.com/api/auth/login"
    data = {"phone": phone,"code": pwd}
    response = request.request(method=method, url=url, data=data)
    res = response.json()
    token = res['data']['access_token']
    # print("token是：{}".format(token))
    return token


# 获取随机的用户名，由6位包括数字，大写，小写字母组成
def rand_name():
    name = ""
    for i in range(6):
        num = random.randint(0, 9)
        # num = chr(random.randint(48,57))  # ASCII表示数字
        letter = chr(random.randint(97, 122))   # 取小写字母
        Letter = chr(random.randint(65, 90))    # 取大写字母
        s = str(random.choice([num, letter, Letter]))
        name += s
    return name


if __name__ == '__main__':
    # token = get_token("15733100728", "123456")
    # print(token)
    name = rand_name()
    print(name)

