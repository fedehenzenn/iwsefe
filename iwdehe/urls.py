from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iwdehe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^inicio/$', 'sitio.views.inicio'),
#    url(r'^accounts/logout/$,', 'django.contrib.auth.view.logout',
#    {'next_page': '/inicio'}),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^solouser/', 'sitio.views.solouser'),
)
