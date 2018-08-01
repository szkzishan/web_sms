#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# Created by kyh on 2017/11/6
from django.contrib.auth.models import Permission
from rest_framework import serializers
from rest_framework.response import Response

from models import *
from django.conf import settings
from rest_framework import exceptions
from django.contrib.auth import get_user_model
from drf_queryfields import QueryFieldsMixin
from guardian.shortcuts import assign_perm
import pinyin
import shortuuid


class SveverBaseSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = SereverModel
        fields = "__all__"


class AppBaseSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = AppModel
        fields = '__all__'


class TableBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableModel
        fields = "__all__"


class FieldBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldModel
        fields = "__all__"


class SveverSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = SereverModel
        fields = "__all__"


class AppSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    table_get = TableBaseSerializer(source="tables", many=True, read_only=True)

    class Meta:
        model = AppModel
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    field_get = FieldBaseSerializer(source='fields', many=True, read_only=True)

    class Meta:
        model = TableModel
        fields = "__all__"
        extra_fields = ["field_get"]


class FieldSerializer(serializers.ModelSerializer):
    table_get = TableBaseSerializer(source='table', read_only=True)

    class Meta:
        model = FieldModel
        fields = "__all__"
        extra_fields = ["table_get"]


class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(use_url=False)

    class Meta:
        model = FileModel
        fields = "__all__"


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ("id", "name",)


class PermissionUserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    permission_id = serializers.IntegerField()

    def save(self, **kwargs):
        user = get_user_model().objects.get(id=self.validated_data.get("user_id"))
        permission = Permission.objects.get(id=self.validated_data.get("permission_id"))
        user.user_permissions.add(permission)
        return Response({"detial": "%s get %s permission" % (user.username, permission.name)})


class GetAppSerializer(serializers.Serializer):
    app_id = serializers.IntegerField()

    def validate_app_id(self, value):
        try:
            AppModel.objects.get(id=value)
            return value
        except Exception, e:
            raise exceptions.ValidationError(e)

    def get_app(self, data):
        print data
        return AppModel.objects.get(id=data.get("app_id"))


class CreateTableSerializer(serializers.Serializer):
    app_name = serializers.ReadOnlyField(source="")
    table_name = serializers.CharField()
    fields = serializers.ListSerializer(child=FieldSerializer())


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
