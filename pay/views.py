# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from pay.serializers import WechatPaySerializer, WeChatPayQuerySerializer
from pay.uitls import WeChatHelper
from wechatpy.pay.utils import dict_to_xml

@api_view(["GET","POST"])
def wechat_notify(request):
    wechat_pay_pay = WeChatHelper().wechatpay()
    data = wechat_pay_pay.parse_payment_result(request.body)
    print data
    return Response(dict_to_xml(dict(return_msg=u"OK",return_code="SUCCESS"),sign=data.get("sign")))

@api_view(["POST"])
def wechat_pay(request):
    serializer = WechatPaySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    datas = serializer.result()
    return Response(datas)

@api_view(["POST"])
def wechat_order_query(request):
    serializer = WeChatPayQuerySerializer(data=request.data)
    data = serializer.result()
    return Response(data)