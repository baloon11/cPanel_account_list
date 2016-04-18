# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from application.views import StartView
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', StartView.as_view(), name='start'),
    url(r'^servers/$', 'application.views.servers',name='servers'),
    url(r'^logout/$', 'application.views.logout',name='logout'),
    url(r'^admin/', include(admin.site.urls))
)
