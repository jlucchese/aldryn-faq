# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from cms.utils.conf import get_cms_setting

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(
        r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT, 'show_indexes': True
        }
    ),
    url(
        r'^media/cms/(?P<path>.*)$',
        'django.views.static.serve',
        {
            'document_root': get_cms_setting('MEDIA_ROOT'),
            'show_indexes': True
        }
    ),
    url(
        r'^jsi18n/(?P<packages>\S+?)/$',
        'django.views.i18n.javascript_catalog'
    ),
)

url_i18n_patterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^faq/', include('aldryn_faq.urls', namespace='aldryn_faq')),
    url(r'^', include('cms.urls')),
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += url_i18n_patterns
