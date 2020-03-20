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


class HTTPRequest(object):

    def __init__(self):
        # 创建session对象
        self.session = Session()

    # 记录cookies信息，给下一次请求使用
    def request(self, method, url, params=None, data=None, headers=None, cookies=None, json=None):
        # 将方法名转化为小写
        method = method.lower()
        if method == "post":
            # 判断是否使用json来传参，适用于接口项目使用json传参
            if json:
                logging.info("正在发送请求，请求地址：{}，请求参数：{}".format(url, json))
                response = self.session.post(url=url, json=json, headers=headers, cookies=cookies)
                return response
            else:
                logging.info("正在发送请求，请求地址：{}，请求参数：{}".format(url, data))
                response = self.session.post(url=url, data=data, headers=headers, cookies=cookies)
                return response
        elif method == "get":
            logging.info("正在发送请求，请求地址：{}，请求参数：{}".format(url, params))
            response = self.session.get(url=url, params=params, headers=headers, cookies=cookies)
            return response

    def close(self):
        self.session.close()


class HTTPRequest1(object):
    # 不记录cookies信息
    def request(self, method, url, params=None, data=None, headers=None, cookies=None, json=None):
        method = method.lower()
        if method == "post":
            if json:
                logging.info("正在发送请求，请求地址：{}，请求参数：{}".format(url, json))
                response = requests.post(url=url, json=json, headers=headers, cookies=cookies)
                return response
            else:
                logging.info("正在发送请求，请求地址：{}，请求参数：{}".format(url, data))
                response = requests.post(url=url, data=data, headers=headers, cookies=cookies)
                return response

        elif method == "get":
            logging.info("正在发送请求，请求地址：{}，请求参数：{}".format(url, params))
            response = requests.get(url=url, params=params, headers=headers, cookies=cookies)
            return response


if __name__ == '__main__':
    r = HTTPRequest()
    url = "http://118.24.221.133:8081/futureloan/mvc/api/member/login"
    method = "post"
    data = {'mobilephone': '13342884220', 'pwd': '123456'}
    response = r.request(method=method, url=url, data=data)
    print(response.status_code)
    print(response.json())







