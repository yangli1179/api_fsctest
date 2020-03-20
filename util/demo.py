# -*- coding: utf-8 -*-
"""

=================================
Author: yangli
Created on: 2020/3/14

E-mail:1179384105@qq.com

=================================


"""


import requests
from requests.sessions import Session
import logging
from common import logger


"""
封装requests类，根据用例中的请求方法，来决定发起什么类型的请求。输出logging日志
"""


class HTTPRequest(object):
    """不记录cookies信息给下一次请求使用"""
    def request(self, method, url,
                params=None, data=None,
                headers=None, cookies=None, json=None):

        method = method.lower()
        if method == "post":
            # 判断是否使用json来传参（适用于接口项目有使用json传参）
            if json:
                logging.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, json))
                return requests.post(url=url, json=json, headers=headers, cookies=cookies)
            else:
                logging.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, data))
                return requests.post(url=url, data=data, headers=headers, cookies=cookies)
        elif method == "get":
            logging.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, params))
            return requests.get(url=url, params=params, headers=headers, cookies=cookies)


class HTTPRequest2(object):
    """记录cookies信息给下一次请求使用"""

    def __init__(self):
        # 创建session对象
        self.session = Session()

    def request(self, method, url,
                params=None, data=None,
                headers=None, cookies=None, json=None):

        method = method.lower()
        if method == "post":
            # 判断是否使用json来传参（适用于接口项目有使用json传参）
            if json:
                logging.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, json))
                return self.session.post(url=url, json=json, headers=headers, cookies=cookies)
            else:
                logging.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, data))
                return self.session.post(url=url, data=data, headers=headers, cookies=cookies)
        elif method == "get":
            logging.info("正在发送请求，请求地址：{}， 请求参数：{}".format(url, params))
            return self.session.get(url=url, params=params, headers=headers, cookies=cookies)

    def close(self):
        self.session.close()


if __name__ == '__main__':
    request = HTTPRequest2()
    url = "http://118.24.221.133:8081/futureloan/mvc/api/member/login"
    method = "post"
    data = {'mobilephone': '13342884220', 'pwd': '123456'}

    response = request.request(method=method, url=url, data=data)
    print(response.json())
    print(type(response.json()))



