from django.conf.urls import url
from django.contrib import admin
import django.contrib.auth.views  as auth_views	
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post.(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$',auth_views.logout, name = 'logout'),
]
