##
from django.conf.urls import url
from . import views
###
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post/new/$',views.post_new,name='post_new'),
    url(r'^post/list/$',views.post_list,name='post_list'),
    url(r'^post/list/(?P<slug>.+)/$',views.post_detail, name='x123'),
    url(r'^menu/(?P<slug>.+)/$',views.post_menu_d,name='total'),
    url(r'^menu/$',views.post_menu,name='total'),    
]
