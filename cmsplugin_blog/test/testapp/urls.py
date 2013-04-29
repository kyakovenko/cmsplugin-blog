from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import patterns, include, url

from cmsplugin_blog.sitemaps import BlogSitemap

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
)


urlpatterns += patterns('',
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {
        'sitemaps': {
            'blogentries': BlogSitemap
        }
    })
)

urlpatterns += i18n_patterns('', url(r'^', include('cms.urls')))
