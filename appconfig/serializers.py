# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 14:42
# @Author  : Aries
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers
from models import ConfigModel,ConfigDataModel

class ConfigDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigDataModel
        fields = "__all__"

class ConfigSerializer(serializers.ModelSerializer):
    config_data_get = ConfigDataSerializer(source="config_data",read_only=True)
    class Meta:
        model = ConfigDataModel
        fields = "__all__"

