# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets,routers
from serializers import *
from models import *

# The Router
router = routers.DefaultRouter()


class TemplateViewSet(viewsets.ModelViewSet):
    serializer_class = TemplateSerializer
    queryset = TemplateModel.objects.all()


router.register('template', TemplateViewSet)


class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    queryset = ModuleModel.objects.all()


router.register('module', ModuleViewSet)


class TableViewSet(viewsets.ModelViewSet):
    serializer_class = TableSerializer
    queryset = TableModel.objects.all()


router.register('table', TableViewSet)


class FieldViewSet(viewsets.ModelViewSet):
    serializer_class = FieldSerializer
    queryset = FieldModel.objects.all()

router.register('field', FieldViewSet)
