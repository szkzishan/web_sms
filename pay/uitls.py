# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time

from django.test import TestCase
from django.conf import settings
# Create your tests here.

# 微信支付
from wechatpy import WeChatPay

class WeChatHelper(object):
    @staticmethod
    def wechatpay():
        wechat_config = {
            "appid": "wx2bc82adb627f16fc",
            "api_key": "yxrs101227SevenStarWeChatpayment",
            "mch_id": "1394986202",
            "mch_cert": "file/wechat/apiclient_cert.pem",
            "mch_key": "file/wechat/apiclient_key.pem",
        }
        return WeChatPay(**wechat_config)

# class AliPayHelper(object):
#     @staticmethod
#     def alipay():
#         app_private_key_string = open("/path/to/your/private/key.pem").read()
#         alipay_public_key_string = open("/path/to/alipay/public/key.pem").read()
#         alipay = AliPay(
#             appid="",
#             app_notify_url="",  # 默认回调url
#             app_private_key_string=app_private_key_string,
#             alipay_public_key_string=alipay_public_key_string,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
#             sign_type="RSA",  # RSA 或者 RSA2
#             debug = False  # 默认False
#         )
#         return alipay
