# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-20 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeeditor', '0005_auto_20171220_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file', verbose_name='\u6587\u4ef6')),
            ],
        ),
        migrations.DeleteModel(
            name='ImageModel',
        ),
    ]
