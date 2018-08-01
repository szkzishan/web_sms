# coding=utf-8
from rest_framework import serializers
from uitls import WeChatHelper

class WechatPaySerializer(serializers.Serializer):
    '''
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
    '''
    trade_type = serializers.CharField()
    body = serializers.CharField()
    total_fee = serializers.IntegerField()
    user_id = serializers.CharField(required=False)
    client_ip = serializers.CharField(required=False)
    out_trade_no = serializers.CharField(required=False)
    detail = serializers.CharField(required=False)
    attach = serializers.CharField(required=False)
    fee_type = serializers.CharField(required=False)
    time_start = serializers.CharField(required=False)
    time_expire = serializers.CharField(required=False)
    goods_tag = serializers.CharField(required=False)
    product_id = serializers.CharField(required=False)
    device_info = serializers.CharField(required=False)
    limit_pay = serializers.CharField(required=False)
    scene_info = serializers.CharField(required=False)

    notify_url = "/pay/wechat_notify"

    def __init__(self,**kwargs):
        super(WechatPaySerializer,self).__init__(**kwargs)
        self.wechatpay = WeChatHelper.wechatpay()
        self.pay_way = {
            "NATIVE": self.order(),
            "JSAPI": self.jsapi(),
        }

    # 统一下单
    def order(self):
        order_data = self.validated_data
        return self.wechatpay.order.create(**order_data)
    # 公众号网页 JS 支付接口
    def jsapi(self):
        order_data = self.order()
        return self.wechatpay.jsapi.get_jsapi_params(
            prepay_id=order_data.get("prepay_id"),
            nonce_str=order_data.get("nonce_str")
        )

    def result(self):
        return self.pay_way.get(self.validated_data("trade_type"))

class WeChatPayQuerySerializer(serializers.Serializer):
    '''
    查询订单

        :param transaction_id: 微信的订单号，优先使用
        :param out_trade_no: 商户系统内部的订单号，当没提供transaction_id时需要传这个。
        :return: 返回的结果数据
    '''
    transaction_id = serializers.CharField(required=False)
    out_trade_no = serializers.CharField(required=False)

    def __init__(self,**kwargs):
        super(WeChatPayQuerySerializer,self).__init__(**kwargs)
        self.wechatpay = WeChatHelper.wechatpay()

    def order_query(self):
        query_data = self.validated_data
        return self.wechatpay.order.query(**query_data)
    def result(self):
        return self.order_query()




