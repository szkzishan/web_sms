# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 10:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeeditor', '0007_auto_20171221_1014'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='fieldmodel',
            unique_together=set([('name', 'table')]),
        ),
        migrations.AlterUniqueTogether(
            name='tablemodel',
            unique_together=set([('name', 'app')]),
        ),
    ]
