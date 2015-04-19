from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iwdehe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'sitio.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'sitio.views.home'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^restricted/', 'sitio.views.restricted'),
)
