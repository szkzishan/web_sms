# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
from django.test import TestCase

# Create your tests here.

# 微信支付
from wechatpy import WeChatPay
from wechatpy.pay import dict_to_xml

"""
微信支付接口

:param appid: 微信公众号 appid
:param api_key: 商户 key
:param mch_id: 商户号
:param sub_mch_id: 可选，子商户号，受理模式下必填                            
:param mch_cert: 必填，商户证书路径
:param mch_key: 必填，商户证书私钥路径
:param timeout: 可选，请求超时时间，单位秒，默认无超时设置
:param sandbox: 可选，是否使用测试环境，默认为 False
"""
wechat_config = {
    "appid":"wx174d12341715ffef",
    "api_key":"haipainongchangweixinzhifu123456",
    "mch_id":"1495392782",
    # "mch_cert":"file/wechat/apiclient_cert.pem",
    # "mch_key":"file/wechat/apiclient_key.pem",
}
wechat_pay = WeChatPay(**wechat_config)
"""
统一下单接口

:param trade_type: 交易类型，取值如下：JSAPI，NATIVE，APP，WAP, MWEB
:param body: 商品描述
:param total_fee: 总金额，单位分
:param notify_url: 接收微信支付异步通知回调地址
:param client_ip: 可选，APP和网页支付提交用户端ip，Native支付填调用微信支付API的机器IP
:param user_id: 可选，用户在商户appid下的唯一标识。trade_type=JSAPI，此参数必传
:param out_trade_no: 可选，商户订单号，默认自动生成
:param detail: 可选，商品详情
:param attach: 可选，附加数据，在查询API和支付通知中原样返回，该字段主要用于商户携带订单的自定义数据
:param fee_type: 可选，符合ISO 4217标准的三位字母代码，默认人民币：CNY
:param time_start: 可选，订单生成时间，默认为当前时间
:param time_expire: 可选，订单失效时间，默认为订单生成时间后两小时
:param goods_tag: 可选，商品标记，代金券或立减优惠功能的参数
:param product_id: 可选，trade_type=NATIVE，此参数必传。此id为二维码中包含的商品ID，商户自行定义
:param device_info: 可选，终端设备号(门店号或收银设备ID)，注意：PC网页或公众号内支付请传"WEB"
:param limit_pay: 可选，指定支付方式，no_credit--指定不能使用信用卡支付
:param scene_info: 可选，上报支付的场景信息
:type scene_info: dict
:return: 返回的结果数据
"""
order_create = {
    "trade_type":"NATIVE",
    "body":"商品测试",
    "total_fee":88,
    # "user_id":"oyRFz007YsAOtal8wt7t7pU_rmDQ",
    "notify_url":"http://haipai-sms.wei7star.com/notify_url",
    # "client_ip":"118.190.68.206",
    # "device_info":"WEB",
    # "product_id":"abcdefg",
    # "out_trade_no":"abcdefg12343421",
}
order = wechat_pay.order.create(**order_create)
print order
jsapi = wechat_pay.jsapi.get_jsapi_params(prepay_id=order.get("prepay_id"),nonce_str=order.get("nonce_str"))
# query = wechat_pay.order.query(out_trade_no="abcdefg123")
print jsapi
# print query
# print order.get("transaction_id")

# print dict_to_xml(dict(return_msg=u"OK",return_code="SUCCESS"),sign="sign")

