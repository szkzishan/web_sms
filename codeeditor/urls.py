#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# Created by kyh on 2017/11/6
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls

import views

urlpatterns = views.router.urls

urlpatterns += [

    url("deploy_app/(?P<operation>\w+)/", views.deploy_app),
    url("app_config/", views.app_config),

]
