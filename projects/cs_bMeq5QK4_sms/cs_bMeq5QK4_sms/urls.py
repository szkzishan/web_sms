# coding:utf-8
"""editor_sms URL Configuration

The `urlpatterns` list routes URLs to view. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function view
    1. Add an import:  from my_app import view
    2. Add a URL to urlpatterns:  url(r'^$', view.home, name='home')
Class-based view
    1. Add an import:  from other_app.view import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^cs_bMeq5QK4/', include("cs_bMeq5QK4.urls", namespace="cs_bMeq5QK4")),
    url(r'^login/', views.obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [url(r'^docs/', include_docs_urls(title=u'测试')), ]

