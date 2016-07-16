# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

__author__ = 'alexy'


urlpatterns = patterns(
    'landing.views',
    url(r'^$', TemplateView.as_view(template_name='landing/index.html'), name='index'),
)
