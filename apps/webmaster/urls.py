# coding=utf-8
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import AdministratorListView

__author__ = 'alexy'

urlpatterns = patterns(
    '',
    url(r'^$', login_required(TemplateView.as_view(template_name='webmaster/quickstats.html')), name='dashboard'),
    url(r'^profile/$', login_required(TemplateView.as_view(template_name='webmaster/profile.html')), name='profile'),
    url(r'^transactions/$', login_required(TemplateView.as_view(template_name='webmaster/transactions.html')), name='transactions'),
    url(r'^payouts/$', login_required(TemplateView.as_view(template_name='webmaster/payouts.html')), name='payouts'),
    url(r'^banners/$', login_required(TemplateView.as_view(template_name='webmaster/banners.html')), name='banners'),
)
