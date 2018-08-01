# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class ConfigModel(models.Model):
    name = models.CharField(verbose_name=u"配置名称",help_text="配置名称",max_length=255)
    table_name = models.CharField(help_text=u"表名",max_length=255)
    field_name = models.CharField(help_text=u"字段名称",max_length=255)
    des = models.TextField(verbose_name=u"描述",help_text=u"描述")

class ConfigDataModel(models.Model):
    config = models.ForeignKey(ConfigModel,help_text=u"配置名",related_name="config_data")
    key = models.CharField(help_text=u"键",max_length=255)
    value = models.CharField(help_text=u"值",max_length=255)