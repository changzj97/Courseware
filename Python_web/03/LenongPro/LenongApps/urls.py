from django.conf.urls import url
from .views import index, goods_list

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^goods_list/$', goods_list,name= 'goods_list'),

]
