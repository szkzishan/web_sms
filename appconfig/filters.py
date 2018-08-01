# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 14:57
# @Author  : Aries
# @Site    : 
# @File    : filters.py
# @Software: PyCharm
from models import *
import rest_framework_filters as filterabc

class ConfigFilter(filterabc.FilterSet):
    class Meta:
        model = ConfigModel
        fields = {u'table_name': '__all__', u'field_name': '__all__'}