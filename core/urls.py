# coding=utf-8
from django.conf.urls import patterns, url
from django.contrib.auth.views import logout
from core.ajax import ajax_remove_item

__author__ = 'alexy'


urlpatterns = patterns(
    'core.views',
    # url(r'^robots\.txt', 'get_robots_txt', name='robots'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^ajax_remove/$', ajax_remove_item, name='ajax-remove'),
)
