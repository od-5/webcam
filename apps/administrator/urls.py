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
    # Webmasters url
    url(r'^webmasters/$', login_required(TemplateView.as_view(template_name='administrator/webmasters/webmster_list.html')), name='webmaster_list'),
    url(r'^webmaster/add/$', login_required(TemplateView.as_view(template_name='administrator/webmasters/webmsater_add.html')), name='webmaster_add'),
    url(r'^webmaster/(?P<pk>\d+)/$', login_required(TemplateView.as_view(template_name='administrator/webmasters/webmstare_update.html')), name='webmaster_update'),
    url(r'^webmasters/banners/$', login_required(TemplateView.as_view(template_name='administrator/webmasters/webmasterbanners.html')), name='webmaster_banners'),
    # Site urls
    url(r'^events/$', login_required(TemplateView.as_view(template_name='administrator/site/event_list.html')), name='event_list'),
    url(r'^event/add/$', login_required(TemplateView.as_view(template_name='administrator/site/event_add.html')), name='event_add'),
    url(r'^sections/$', login_required(TemplateView.as_view(template_name='administrator/site/section_list.html')), name='section_list'),
    url(r'^section/(?P<pk>\d+)/$', login_required(TemplateView.as_view(template_name='administrator/site/material_list.html')), name='material_list'),
    url(r'^material/add/$', login_required(TemplateView.as_view(template_name='administrator/site/material_add.html')), name='material_add'),
    url(r'^material/(?P<pk>\d+)/$', login_required(TemplateView.as_view(template_name='administrator/site/material_update.html')), name='material_update'),
    # Config urls
    url(r'^systemconfig/$', login_required(TemplateView.as_view(template_name='administrator/config/systemconfig.html')), name='systemconfig'),
    url(r'^workers/$', login_required(TemplateView.as_view(template_name='administrator/config/worker_list.html')), name='worker_list'),
    url(r'^archive/$', login_required(TemplateView.as_view(template_name='administrator/config/archive_list.html')), name='archive_list'),
    url(r'^paymentpackages/$', login_required(TemplateView.as_view(template_name='administrator/config/paymentpackages_list.html')), name='paymentpackages_list'),
    url(r'^newsletters/$', login_required(TemplateView.as_view(template_name='administrator/config/newsletter_list.html')), name='newsletter_list'),
    url(r'^paymentcoupons/$', login_required(TemplateView.as_view(template_name='administrator/config/paymentcoupon_list.html')), name='paymentcoupon_list'),
    url(r'^cameras/$', login_required(TemplateView.as_view(template_name='administrator/config/camera_list.html')), name='camera_list'),
    url(r'^camera/add/$', login_required(TemplateView.as_view(template_name='administrator/config/camera_add.html')), name='camera_add'),
    url(r'^camera/(?P<pk>\d+)/$', login_required(TemplateView.as_view(template_name='administrator/config/camera_update.html')), name='camera_update'),
    url(r'^profile/$', login_required(TemplateView.as_view(template_name='administrator/config/profile.html')), name='profile'),
    url(r'^pages/$', login_required(TemplateView.as_view(template_name='administrator/config/page_list.html')), name='page_list'),
    url(r'^pages/add/$', login_required(TemplateView.as_view(template_name='administrator/config/page_add.html')), name='page_add'),
    url(r'^pages/(?P<pk>\d+)/$', login_required(TemplateView.as_view(template_name='administrator/config/page_update.html')), name='page_update'),
)
