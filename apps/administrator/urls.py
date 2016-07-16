# coding=utf-8
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import AdministratorListView

__author__ = 'alexy'

urlpatterns = patterns(
    '',
    # url(r'^moderator/$', 'moderator_sign', name='moderator'),
    # url(r'^manager/$', 'manager_sign', name='manager'),
    # url(r'^client/$', 'client_sign', name='client'),
    # url(r'^adjuster/$', 'adjuster_sign', name='adjuster'),
    url(r'^$', login_required(TemplateView.as_view(template_name='administrator/administrator_dashboard.html')), name='dashboard'),
    url(r'^quickstats/$', login_required(TemplateView.as_view(template_name='administrator/statistic/quickstats.html')), name='quickstats'),
    url(r'^refererstats/$', login_required(TemplateView.as_view(template_name='administrator/statistic/refererstats.html')), name='refererstats'),
    url(r'^webmasterstats/$', login_required(TemplateView.as_view(template_name='administrator/statistic/webmasterstats.html')), name='webmasterstats'),
    url(r'^livestats/$', login_required(TemplateView.as_view(template_name='administrator/statistic/livestats.html')), name='livestats'),
)
