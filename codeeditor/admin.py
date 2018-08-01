# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.contrib import admin

# Register your model here.
class FieldInline(admin.StackedInline):
    model = FieldModel

class TableInline(admin.TabularInline):
    model = TableModel

@admin.register(AppModel)
class AppAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name','created')
    inlines = [
        TableInline,
        # FieldInline,
    ]

