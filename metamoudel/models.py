# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

USER = User


# Create your models here.
# 模板
class TemplateModel(models.Model):
    name = models.CharField(help_text=u"名字", max_length=255)
    category = models.CharField(help_text=u"类别", max_length=255)
    des = models.TextField(help_text=u"简介")
    create_time = models.DateTimeField(help_text=u"创建时间", auto_now=True)
    creator = models.ForeignKey(USER, help_text=u"创建者")


# 模块
class ModuleModel(models.Model):
    name = models.CharField(help_text=u"名字", max_length=255)
    des = models.TextField(help_text=u"简介")
    template = models.ForeignKey(TemplateModel, help_text=u"模板_id", related_name=u"modules")
    create_time = models.DateTimeField(help_text=u"创建时间", auto_now=True)
    creator = models.ForeignKey(USER, help_text=u"创建者")


# 功能
class FunctionModel(models.Model):
    name = models.CharField(help_text=u"名字", max_length=255)
    des = models.TextField(help_text=u"简介")
    module = models.ForeignKey(ModuleModel, help_text=u"模块_id", related_name=u"functions")
    tables = models.ManyToManyField("TableModel",related_name="functions")


# table
class TableModel(models.Model):
    name = models.CharField(help_text=u"名字", max_length=255)
    des = models.TextField(help_text=u"简介")
    # module = models.ForeignKey(ModuleModel, help_text=u"模块_id", related_name=u"tables")



# field
class FieldModel(models.Model):
    name = models.CharField(help_text=u"名字", max_length=255)
    des = models.TextField(help_text=u"简介")
    placeholder = models.TextField(help_text=u"描述")
    table = models.ForeignKey(TableModel, help_text=u"table_id", related_name=u"fields")
    genre = models.CharField(help_text=u"后端类型", max_length=255)
    widget = models.CharField(help_text=u"前段部件", max_length=255)
    default_value = models.CharField(help_text=u"默认值", max_length=255)
    foreign_model = models.CharField(help_text=u"外键参数", max_length=255)
    is_null = models.BooleanField(help_text=u"是否为空")
    is_search = models.BooleanField(help_text=u"是否搜索")
    is_abstract = models.BooleanField(help_text=u"是否创建")
    filter_terms = models.CharField(help_text=u"查询条件", max_length=255)
    error_msg = models.CharField(help_text=u"校验错误提示", max_length=255)
    verify = models.CharField(help_text=u"字段校验", max_length=255)
