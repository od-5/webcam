# coding=utf-8
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import debug_toolbar


urlpatterns = patterns(
    '',
    # url(r'^administrator/', include('apps.administrator.urls', namespace='administrator'),),
    url(r'^sign/', include('apps.sign.urls', namespace='sign'),),
    url(r'^cabinet/', include('cabinet.urls', namespace='cabinet'),),
    url(r'', include('landing.urls', namespace='landing')),
    url(r'', include('core.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
