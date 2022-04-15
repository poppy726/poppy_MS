"""
@author:poppy
@time:2022/4/14 15:55
"""
import json
import random
import re

import requests


class TestWechatApi:

    access_token = ""
    id = ""

    def test_get_token(self):
        urls = "https://api.weixin.qq.com/cgi-bin/token"
        datas = {
            "grant_type": "client_credential",
            "appid": "",
            "secret": ""
        }
        res = requests.request("get", url=urls, params=datas)
        TestWechatApi.access_token = res.json()["access_token"]
        # print(res.json())
        print(TestWechatApi.access_token)


    def test_get_tag(self):
        urls = "https://api.weixin.qq.com/cgi-bin/tags/get?access_token="+TestWechatApi.access_token
        res = requests.request("get",url=urls)
        print(res.json())
        # print(res) # 打印响应码200
        return res


    def test_create_tag(self):
        urls = "https://api.weixin.qq.com/cgi-bin/tags/create?access_token="+TestWechatApi.access_token
        datas = {"tag":{"name":"长沙"+str(random.randint(10000,99999))}}
        res = requests.request("post",url=urls,json=datas)
        print(json.loads(json.dumps(res.json()).replace(r"\\","\\")))

    def test_edit_tag(self):
        urls = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token="+TestWechatApi.access_token
        datas = {"tag":{"id":227,"name":"广东"+str(random.randint(10000,99999))}}
        res = requests.request("post",url=urls,json=datas)
        print(res.json)


    def test_delete_tag(self):
        urls = "https://api.weixin.qq.com/cgi-bin/tags/delete?access_token="+TestWechatApi.access_token
        datas = {"tag":{"id": 227}}
        res = requests.request("post",url=urls,json=datas)
        print(res.json())

    def test_upload_file(self):
        urls = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token="+TestWechatApi.access_token
        datas = {"media": open(r"E:\\shu.png",'rb')}
        res = requests.request("post",url=urls,files=datas)
        print(res.json)




