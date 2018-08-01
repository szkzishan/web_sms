# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from serializers import WechatPaySerializer, WeChatPayQuerySerializer
from uitls import WeChatHelper
from wechatpy.pay.utils import dict_to_xml


# 付款回掉
@api_view(["GET", "POST"])
def wechat_notify(request):
    wechat_pay_pay = WeChatHelper().wechatpay()
    data = wechat_pay_pay.parse_payment_result(request.body)
    print data
    return Response(dict_to_xml(dict(return_msg=u"OK", return_code="SUCCESS"), sign=data.get("sign")))


# 付款
@api_view(["POST"])
def wechat_pay(request):
    serializer = WechatPaySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    datas = serializer.result()
    return Response(datas)


# 订单查询
@api_view(["POST"])
def wechat_order_query(request):
    serializer = WeChatPayQuerySerializer(data=request.data)
    data = serializer.result()
    return Response(data)

# oauth
@api_view(["GET"])
def wechat_oauth(request):
    return Response(WeChatHelper.wechat_oauth().authorize_url)

# oauth 回调
@api_view(["GET", "POST"])
def wechat_oauth_callback(request):
    print request.body
    pass

