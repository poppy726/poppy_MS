"""
@author:poppy
@time:2022/4/14 18:23
"""
import requests
import re



class TestPhpwindApi:

    csrf_token = ""

    php_session = requests.session()

    def test_phpwind_index(self):
        urls = "http://47.107.116.139/phpwind/"
        res = TestPhpwindApi.php_session.request("get",url=urls)

        TestPhpwindApi.csrf_token = re.search('name="csrf_token" value="(.*?)"', res.text).group(1)
        print(TestPhpwindApi.csrf_token)


    def test_phpwind_login(self):
        urls = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        datas ={
            "username":"poppy",
            "password":"123456",
            "csrf_token":TestPhpwindApi.csrf_token,
            "backurl":"http://47.107.116.139/phpwind/",
            "invite":""
        }
        headers = {
            "Accept":"application/json,text/javascript,/;q=0.01",
            "X-Requested-With":"XMLHttpRequest"
        }

        res = TestPhpwindApi.php_session.request("post",url=urls,data=datas,headers=headers)
        print(res.text)


