# -*- coding: utf-8 -*-
import coreapi
from coreapi import Client
import requests
import urlparse

# 短信测试
class YiYuanSms(object):
    headers = {
        "Authorization": "APPCODE 34b9048d5ff04aabbdf5067f2315f442",
    }
    host = 'http://ali-sms.showapi.com'
    path = ''
    params = {}
    def do_request(self):
        return requests.get(urlparse.urljoin(self.host,self.path),headers=self.headers,params=self.params)
    def query_template(self):
        self.path = "/searchTemplate"
        response = self.do_request()
        print response.text

    def create_template(self):
        pass


    def send_sms(self,tel,code):
        self.path = "/sendSms"
        self.params = {
            "mobile": tel,
            "tNum": "T170317001798",
            "content": '{"code": "%s"}' % code,
        }
        response = self.do_request().json()
        print response
        flag = response.get("showapi_res_body",{}).get("ret_code")
        remark = response.get("showapi_res_body",{}).get("remark")
        return flag,remark


if __name__ == '__main__':
    yys = YiYuanSms()
    print yys.send_sms("15552290166","123456")
