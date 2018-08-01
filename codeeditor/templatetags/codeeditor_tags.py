#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# Created by kyh on 2017/12/8
from django.template.defaulttags import register

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)