# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from landing.models import Setup

__author__ = 'alexy'


class LandingView(TemplateView):
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data()
        setup = Setup.objects.first()
        context.update({
            'SETUP': setup
        })
        return context


def get_robots_txt(request):
    """
    Функция отображения robots.txt
    """
    setup = Setup.objects.first()
    try:
        content = setup.robots_txt
    except:
        content = u'User-agent: *'
    return HttpResponse(content, content_type='text/plain')


def get_sitemap_xml(request):
    """
    Функция отображения sitemap.xml
    """
    setup = Setup.objects.first()
    try:
        content = setup.sitemap
    except:
        content = u'User-agent: *'
    return HttpResponse(content, content_type='text/xml')

