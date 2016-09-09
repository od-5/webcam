# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .ajax import ticket_send
from .views import LandingView

__author__ = 'alexy'


urlpatterns = patterns(
    'landing.views',
    url(r'^$', LandingView.as_view(), name='index'),
    url(r'^site/$', TemplateView.as_view(template_name='landing/site.html'), name='site'),
    url(r'^site/mobile/$', TemplateView.as_view(template_name='landing/site_mobile.html'), name='site-mobile'),
    url(r'^site/tablet/$', TemplateView.as_view(template_name='landing/site_tablet.html'), name='site-tablet'),
    url(r'^thnx/$', TemplateView.as_view(template_name='landing/ok.html'), name='thnx'),
    url(r'^ticket_send/$', ticket_send, name='ticket'),
    url(r'^robots\.txt', 'get_robots_txt', name='robots'),
    url(r'^sitemap\.xml', 'get_sitemap_xml', name='sitemap'),
)
