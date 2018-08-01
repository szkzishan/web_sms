# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,routers
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_filters.backends import DjangoFilterBackend

from appconfig.filters import ConfigFilter
from models import ConfigDataModel,ConfigModel
from serializers import *

router = routers.DefaultRouter()
class ConfigViewSet(viewsets.ModelViewSet):
    queryset = ConfigModel.objects.all()
    serializer_class = ConfigSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filter_class = ConfigFilter
router.register(r'config', ConfigViewSet, base_name='config')

class ConfigDataViewSet(viewsets.ModelViewSet):
    queryset = ConfigDataModel.objects.all()
    serializer_class = ConfigDataSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
router.register(r'configdata', ConfigViewSet, base_name='configdata')