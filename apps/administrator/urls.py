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
    # Statictic urls
    url(r'^quickstats/$', login_required(TemplateView.as_view(template_name='administrator/statistic/quickstats.html')), name='quickstats'),
    url(r'^refererstats/$', login_required(TemplateView.as_view(template_name='administrator/statistic/refererstats.html')), name='refererstats'),
    url(r'^webmasterstats/$', login_required(TemplateView.as_view(template_name='administrator/statistic/webmasterstats.html')), name='webmasterstats'),
    url(r'^livestats/$', login_required(TemplateView.as_view(template_name='administrator/statistic/livestats.html')), name='livestats'),
    # Customers url
    url(r'^customers/$', login_required(TemplateView.as_view(template_name='administrator/customers/customer_list.html')), name='customer_list'),
    url(r'^customer/(?P<pk>\d+)/$', login_required(TemplateView.as_view(template_name='administrator/customers/customer_update.html')), name='customer_update'),
    url(r'^customer/add/$', login_required(TemplateView.as_view(template_name='administrator/customers/customer_add.html')), name='customer_add'),
    url(r'^blockedlocations/$', login_required(TemplateView.as_view(template_name='administrator/customers/blockedlocations.html')), name='blockedlocations'),
    url(r'^membershiptransactions/$', login_required(TemplateView.as_view(template_name='administrator/customers/membershiptransactions.html')), name='membershiptransactions'),
    url(r'^chatlogs/$', login_required(TemplateView.as_view(template_name='administrator/customers/chatlogs.html')), name='chatlogs'),
    url(r'^chatlog/(?P<pk>\d+)$', login_required(TemplateView.as_view(template_name='administrator/customers/chatlog.html')), name='chatlog'),
    url(r'^badwords/$', login_required(TemplateView.as_view(template_name='administrator/customers/badwords.html')), name='badwords'),
)
