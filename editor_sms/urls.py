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
import codeeditor
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^codeeditor/', include("codeeditor.urls", namespace="codeeditor")),
                  url(r'^pay/', include("pay.urls", namespace="pay")),
                  url(r'^login/', views.obtain_auth_token),
                  url(r'^meatecode/', include("metamoudel.urls",namespace="meatecode")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [url(r'^docs/', include_docs_urls(title=u'元数据编辑器')), ]
