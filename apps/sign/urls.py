# coding=utf-8
from django.conf.urls import patterns, url
from django.contrib.auth.views import logout

__author__ = 'alexy'

urlpatterns = patterns(
    'apps.sign.views',
    url(r'^$', 'sign_in', name='login'),
    # url(r'^administratpr/$', 'sign_in', {'usertype': 2}, name='moderator'),
    # url(r'^client/$', 'sign_in', {'usertype': 3},  name='client'),
    # url(r'^adjuster/$', 'sign_in', {'usertype': 4}, name='adjuster'),
    # url(r'^manager/$', 'sign_in', {'usertype': 5},  name='manager'),
    url(r'^logout/$', logout, name='logout'),
)
