# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeeditor', '0006_auto_20171220_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appmodel',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
