# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 16:43
# @Author  : Aries
# @Site    : 
# @File    : uitls.py
# @Software: PyCharm
import wechatpy
from django.conf import settings


class WeChatHelper(object):
    @staticmethod
    def wechatpay():
        return wechatpy.WeChatPay(
            appid='',
            api_key='',
            mch_id='',
            mch_cert='',
            mch_key='',
        )

    @staticmethod
    def wechat_oauth():
        return wechatpy.oauth.WeChatOAuth(
            app_id=settings.WECHAT_APP_ID,
            secret=settings.WECHAT_SECRET,
            redirect_uri=settings.WECHAT_OAUTH_REDIRECT_URI,
            # scope="",
            # state="",
        )