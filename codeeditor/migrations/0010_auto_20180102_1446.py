# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-02 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeeditor', '0009_serevermodel_host_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appmodel',
            name='server_port',
            field=models.IntegerField(blank=True, verbose_name='\u542f\u52a8\u7aef\u53e3'),
        ),
    ]
