# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class OrderModel(models.Model):
    '''
    订单表
      用户
      商品
      订单号
      创建时间
    '''
    user = models.ForeignKey(User,help_text="用户外键",related_name="user_order")
    goods_id = models.IntegerField(help_text=u"商品id")
    order_num = models.CharField(max_length=255,help_text=u"订单号")
    create_time = models.DateTimeField(auto_now=True,help_text=u"创建时间")

    pass
