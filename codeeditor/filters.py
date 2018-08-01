#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# Created by kyh on 2017/11/22
from models import *
import rest_framework_filters as filters
from rest_framework.filters import SearchFilter, BaseFilterBackend


class AppFilter(filters.FilterSet):
    class Meta:
        model = AppModel
        fields = "__all__"

class TableFilter(filters.FilterSet):
    class Meta:
        model = TableModel
        fields = "__all__"


class FieldFilter(filters.FilterSet):
    class Meta:
        model = FieldModel
        fields = "__all__"

class IsOwnerFilterBackend(BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(user=request.user)