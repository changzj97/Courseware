from django.conf.urls import url
from .views import index, goods_list, detail

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^goods_list/(?P<tid>\d+)/$', goods_list, name='goods_list'),
    url(r'^detail/(?P<gid>\d+)/$', detail, name='detail'),

]
