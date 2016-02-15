from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crawler.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^beauty_salon/', include('crawler.beauty_salon.urls')),
)
