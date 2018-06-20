from django.conf.urls import url
from .views import index, goods_list, detail, ajax_test, ajax_handle, addshow, add_handele, Search_handle

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^goods_list/(?P<tid>\d+)/$', goods_list, name='goods_list'),
    url(r'^detail/(?P<gid>\d+)/$', detail, name='detail'),
    url(r'^ajax_test/$', ajax_test, name='ajax_test'),
    url(r'^ajax_handle/$', ajax_handle, name='ajax_handle'),
    url(r'^add_show/$', addshow, name='addshow'),
    url(r'^add_handle/$', add_handele, name='add_handle'),
    url(r'^search/', Search_handle.as_view(), name='search')

]
