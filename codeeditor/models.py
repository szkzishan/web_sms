# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pinyin
import shortuuid
from django.db import models

from django.contrib.auth.models import User, AbstractUser
from simple_history.models import HistoricalRecords


# Create your model here.

class SereverModel(models.Model):
    host_name = models.CharField(verbose_name=u"主机名称", max_length=50, blank=True)
    host_ip = models.GenericIPAddressField(verbose_name=u"主机地址")
    host_port = models.IntegerField(verbose_name=u"主机端口", default=22)
    host_user = models.CharField(verbose_name=u"用户名", help_text=u"不推荐使用root", max_length=50)
    host_password = models.CharField(verbose_name=u"用户密码", max_length=255)
    project_path = models.CharField(verbose_name=u"工程路径", max_length=255, help_text=u"默认用户主目录projects",
                                    default="~/projects")
    user = models.ForeignKey(User, related_name="user_servers")
    history = HistoricalRecords()

    class Meta:
        permissions = (
            ('view_serevermodel', 'View SereverModel'),
        )


class AppModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    des = models.CharField(max_length=25, blank=True, null=True)
    img_path = models.CharField(max_length=255, blank=True, null=True)
    server = models.ForeignKey(SereverModel, related_name="server_apps", blank=True, null=True)
    server_port = models.IntegerField(verbose_name=u"启动端口", blank=True)
    created = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name="user_apps", blank=True, null=True)
    create_time = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def table_init(self):
        user_table, _ = TableModel.objects.get_or_create(des=u"用户表", app=self)
        user_table.name = "user"
        user_table.save()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id and not self.name and self.des:
            self.name = pinyin.get_initial(self.des).replace(" ", "") + "_" + shortuuid.ShortUUID().random(8)
        if not self.server:
            self.server = SereverModel.objects.get(id=4)
        if not self.server_port:
            self.server_port = 8000
            port_exists = AppModel.objects.filter(server=self.server, server_port=self.server_port).exists()
            print port_exists
            while port_exists:
                self.server_port = self.server_port + 10
                port_exists = AppModel.objects.filter(server=self.server, server_port=self.server_port).exists()
        super(AppModel, self).save()
        self.table_init()

    def __unicode__(self):
        return self.des


class AppSetModel(models.Model):
    app = models.ForeignKey(AppModel, related_name="app_set")
    app_set = models.CharField(help_text=u"新增app", max_length=255)
    des = models.TextField(help_text=u"描述")


class TableModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    des = models.CharField(max_length=25, blank=True, null=True)
    app = models.ForeignKey(AppModel, related_name="tables", blank=True, null=True)
    is_history = models.BooleanField(verbose_name=u"是否保存操作记录",default=False)
    history = HistoricalRecords()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id and not self.name and self.des:
            self.name = pinyin.get_initial(self.des).replace(" ", "") + "_" + shortuuid.ShortUUID().random(8)
        super(TableModel, self).save()

    def __unicode__(self):
        return self.des

    class Meta:
        unique_together = ("name", "app")
        permissions = (
            ('view_tablemodel', 'View TableModel'),
        )


# widgets = [
#     { value: 'text', label: '文本框' },
#     { value: 'text_area', label: '文本域' },
#     { value: 'markdown', label: 'markdown' },
#     { value: 'number', label: '数字'},
#     { value: 'boolean', label: '布尔值' },
#     { value: 'slider', label: '滑块' },
#     { value: 'radio', label: '单选框'},
#     { value: 'check_box', label: '多选框' },
#     { value: 'select', label: '下拉框'},
#     { value: 'date', label: '日期' },
#     { value: 'img', label: '图片' },
#     { value: 'imgGroup', label: '图片组'},
# ];

widget = {
    "text": "CharField",
    "text_area": "TextField",
    "markdown": "TextField",
    "number_float": "FloatField",
    "number_int": "IntegerField",
    "boolean": "BooleanField",
    "slider": "CharField",
    "radio": "CharField",
    "check_box": "CharField",
    "select": "CharField",
    "date": "DateTimeField",
    "img": "CharField",
    "imgGroup": "CharField",
    "ganged": "ForeignKey",
}

UERY_TERMS = {
    'exact',  # 精确匹配 大小写敏感
    'iexact',  # 非精确匹配 大小写不敏感
    'contains',  # 包含
    'icontains',  # 不包含  大小写不敏感
    'gt',  # 大于
    'gte',  # 大于等于
    'lt',  # 小于
    'lte',  # 小小于等于
    'in',  # in list
    'startswith',  # 头部匹配
    'istartswith',  # 头部匹配 大小写不敏感
    'endswith',  # 尾部匹配
    'iendswith',  # 尾部匹配 大小写不敏感
    'range',  #
    # 对于时间查询
    'year',
    'month',
    'day',
    'week_day',
    'hour',
    'minute',
    'second',

    'isnull',  # 为空
    'search',  #
    'regex',  # 正则
    'iregex',  # 正则 大小写不敏感
}


class FieldModel(models.Model):
    name = models.CharField(verbose_name=u"名字",max_length=255, blank=True, null=True)
    des = models.CharField(verbose_name=u"描述",max_length=255, blank=True, null=True)
    genre = models.CharField(verbose_name=u"类型",max_length=50, blank=True, null=True)
    param = models.CharField(verbose_name=u"参数",max_length=255, blank=True, null=True)
    table = models.ForeignKey(TableModel,verbose_name=u"所属表格", related_name="fields", blank=True, null=True)
    is_null = models.BooleanField(default=True, help_text=u"是否为空")
    is_filter = models.BooleanField(default=False, help_text=u"允许筛选")
    is_search = models.BooleanField(default=False, help_text=u"允许搜索")
    default_value = models.CharField(verbose_name=u"默认值", max_length=255, blank=True, null=True)
    choices_value = models.TextField(verbose_name=u"选择内容", blank=True, null=True)
    widget = models.CharField(verbose_name=u"部件", max_length=255, blank=True, null=True)
    filters = models.CharField(verbose_name=u"筛选条件", max_length=255, blank=True, null=True)
    is_abstract = models.BooleanField(verbose_name=u"是否创建", default=False)
    history = HistoricalRecords()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id and not self.name and self.des:
            self.name = pinyin.get_initial(self.des).replace(" ", "") + "_" + shortuuid.ShortUUID().random(8)
        self.genre = widget.get(self.widget)
        super(FieldModel, self).save()

    class Meta:
        unique_together = ("name", "table")
        permissions = (
            ('view_fieldmodel', 'View FieldModel'),
        )


class FileModel(models.Model):
    file = models.FileField(verbose_name=u"文件", help_text=u"", upload_to="file")
    history = HistoricalRecords()
