# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-12 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeeditor', '0012_fieldmodel_choices_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldmodel',
            name='des',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
