#-*- coding:utf-8 -*-
'''Zheng 's BUG'''
from rango import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name = 'index'),  # 传到这一级 空字符就是默认页
    url(r'^about/', views.about, name = 'about'),
    url(r'^add_category/$', views.add_category, name ='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name = 'add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name = 'show_category'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
]

