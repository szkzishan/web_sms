import views
from django.conf.urls import url, include
urlpatterns = views.router.urls
urlpatterns += [
    url(r'^get_user_id/', views.get_user_id),
]
