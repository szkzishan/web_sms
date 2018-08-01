# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import *
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
from rest_framework.response import Response
# base_template

class userBaseSerializer(serializers.ModelSerializer):
    '''
    user Serializer
    '''
    class Meta:
        model = userModel
        fields = "__all__"


class by_2mF4HV9zBaseSerializer(serializers.ModelSerializer):
    '''
    by_2mF4HV9z Serializer
    '''
    class Meta:
        model = by_2mF4HV9zModel
        fields = "__all__"


class be_hbigt2yMBaseSerializer(serializers.ModelSerializer):
    '''
    be_hbigt2yM Serializer
    '''
    class Meta:
        model = be_hbigt2yMModel
        fields = "__all__"



# serializer_template
# %(table_name)s

class by_2mF4HV9zSerializer(serializers.ModelSerializer):
    '''
    by_2mF4HV9z
    '''
    
    student_name_get = be_hbigt2yMBaseSerializer(source='student_name',read_only=True)
    
    field_03_get = be_hbigt2yMBaseSerializer(source='field_03',read_only=True)
    
    
    class Meta:
        model = by_2mF4HV9zModel
        fields = "__all__"
        extra_fields = [u'student_name_get', u'field_03_get']

class userSerializer(serializers.ModelSerializer):
    '''
    user
    '''
    
    
    class Meta:
        model = userModel
        fields = "__all__"
        extra_fields = []

class be_hbigt2yMSerializer(serializers.ModelSerializer):
    '''
    be_hbigt2yM
    '''
    
    
    by_2mF4HV9z_student_name_get = by_2mF4HV9zBaseSerializer(source='by_2mF4HV9z_student_name',read_only=True,many=True)
    
    by_2mF4HV9z_field_03_get = by_2mF4HV9zBaseSerializer(source='by_2mF4HV9z_field_03',read_only=True,many=True)
    
    class Meta:
        model = be_hbigt2yMModel
        fields = "__all__"
        extra_fields = [u'student_name_get', u'field_03_get']



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

class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(use_url=False)
    class Meta:
        model = FileModel
        fields = "__all__"
