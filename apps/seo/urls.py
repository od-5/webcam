# coding=utf-8
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import AdministratorListView

__author__ = 'alexy'

urlpatterns = patterns(
    '',
    url(r'^$', login_required(TemplateView.as_view(template_name='seo/page_list.html')), name='dashboard'),
    url(r'^add/$', login_required(TemplateView.as_view(template_name='seo/page_add.html')), name='page_add'),
    url(r'^(?P<pk>\d+)/$', login_required(TemplateView.as_view(template_name='seo/page_update.html')), name='page_update'),
    url(r'^profile/$', login_required(TemplateView.as_view(template_name='seo/profile.html')), name='profile'),
)
