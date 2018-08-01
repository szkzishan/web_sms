#!/usr/bin/env python
# encoding: utf-8

"""
@author: kyh
@software: PyCharm
@file: serializers.py
@time: 18-2-7 下午2:04
"""

from rest_framework import serializers
from models import *


class TemplateSerializer(serializers.Serializer):
    class Meta:
        model = TemplateModel
        fields = "__all__"


class ModuleSerializer(serializers.Serializer):
    class Meta:
        model = ModuleModel
        name = 'module'
        fields = "__all__"


class TableSerializer(serializers.Serializer):
    class Meta:
        model = TableModel
        name = 'table'
        fields = "__all__"


class FieldSerializer(serializers.Serializer):
    class Meta:
        model = FieldModel
        name = 'field'
        fields = "__all__"
