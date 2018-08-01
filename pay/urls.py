from django.conf.urls import url
import views
urlpatterns = [
    url("wechat_notify",views.wechat_notify,name="wechat_notify"),
    url("wechat_pay",views.wechat_pay,name="wechat_pay"),
    url("wechat_order_query",views.wechat_order_query,name="wechat_order_query"),
]