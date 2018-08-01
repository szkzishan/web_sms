# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User,AbstractUser

#  Model


class by_2mF4HV9zModel(models.Model):
    '''
    by_2mF4HV9z Model
    '''

    zdy_vyoigDw6 = models.TextField(blank=True, null=True,help_text=u'字段一')

    student_name = models.ForeignKey('be_hbigt2yMModel', related_name='by_2mF4HV9z_student_name',help_text=u'学生姓名',blank=True, null=True)

    field_03 = models.ForeignKey('be_hbigt2yMModel', related_name='by_2mF4HV9z_field_03',help_text=u'字段二',blank=True, null=True)


    class Meta:
        permissions = (
            ('view_by_2mF4HV9zmodel', 'View by_2mF4HV9zModel'),
        )


class userModel(AbstractUser):
    '''
    user Model
    '''


    class Meta:
        permissions = (
            ('view_usermodel', 'View userModel'),
        )


class be_hbigt2yMModel(models.Model):
    '''
    be_hbigt2yM Model
    '''


    class Meta:
        permissions = (
            ('view_be_hbigt2yMmodel', 'View be_hbigt2yMModel'),
        )

class FileModel(models.Model):
    file = models.FileField(verbose_name=u"文件", help_text=u"", upload_to="file")
