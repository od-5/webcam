# coding=utf-8
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from .views import WelcomeView

__author__ = 'alexy'

urlpatterns = patterns(
    'cabinet.views',
    url(r'^$', 'cabinet_sign', name='welcome'),
    url(r'^contacts/$', TemplateView.as_view(template_name='cabinet/contacts.html'), name='contacts'),
    url(r'^terms/$', TemplateView.as_view(template_name='cabinet/terms.html'), name='terms'),

    url(r'^administrator/', include('apps.administrator.urls', namespace='administrator'),),
    url(r'^webmaster/', include('apps.webmaster.urls', namespace='webmaster'),),
    url(r'^seo/', include('apps.seo.urls', namespace='seo'),),
)
