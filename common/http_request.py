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
        elif method == "put":
            logging.info("正在发送请求，请求地址：{}，请求参数：{}".format(url, data))
            response = self.session.put(url=url, data=data, headers=headers, cookies=cookies)
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
        elif method == "put":
            if json:
                logging.info("正在发送请求，请求地址：{}，请求参数：{}".format(url, json))
                response = requests.put(url=url, json=json, headers=headers, cookies=cookies)
                return response
            logging.info("正在发送请求，请求地址：{}，请求参数：{}".format(url, data))
            response = requests.put(url=url, data=data, headers=headers, cookies=cookies)
            return response


if __name__ == '__main__':
    r = HTTPRequest1()
    # url = "http://118.24.221.133:8081/futureloan/mvc/api/member/login"
    # method = "post"
    # data = {'mobilephone': '13342884220', 'pwd': '123456'}
    # response = r.request(method=method, url=url, data=data)
    # print(response.status_code)
    # print(response.json())
    url = "https://fsc-test.manshang.com/api/seller-setting/21"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvZnNjLXRlc3QubWFuc2hhbmcuY29tXC9hcGlcL2F1dGhcL3JlZnJlc2giLCJpYXQiOjE1ODU0NjAyMjIsImV4cCI6MTU4NTc1MjExOSwibmJmIjoxNTg1NzQ4NTE5LCJqdGkiOiJIM0twZ0NlVmF1YWxPNDNEIiwic3ViIjo3NywicHJ2IjoiODY4MDg3YjE4M2IzN2E2OTQ5NDgwMGNhMDE2MjI0Y2FiNWNhNGJjMyJ9.6M34u7KSFDkTplJ8Ky7oBy2z0ciF0mIjOvLaw7rPAAA",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Referer": "https://fsc-test.manshang.com/app/invoice/ApplyDetail/Apply",
        "Origin": "https://fsc-test.manshang.com",
        "Accept-Encoding": "gzip, deflate, br"}
    data = {'name': '客户022落落零零落落零零落落啦啦啦', "id": 21, "customer_id": 34, "company_id": 22, "duty_paragraph": "222", "address": "地址222",
            "phone": "15733100728",
            "bank_name": "222", "card_no": "222", "payee": "222", "reviewer": "222", "drawer": "222"}
    response = requests.put(url=url, data=data, headers=headers)
    print(response.json())



