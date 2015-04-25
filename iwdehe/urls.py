from django.conf.urls import patterns, include, url
from django.contrib import admin
from forum.views import review_create, review_update, review_listing, review_delete, review_detail


urlpatterns = patterns('',
    url(r'^$', 'sitio.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'sitio.views.home'),
    url(r'^home/account/', include('allauth.urls')),
    url(r'^home/account/logout/', 'django.contrib.auth.views.logout', {'next_page': 'home/'}),
    url(r'^restricted/', 'sitio.views.restricted'),
    url(r'^home/list/$', review_listing.as_view(), name='listing'),
    url(r'^home/create/$', review_create.as_view(), name='create'),
    url(r'^home/list/(?P<pk>\d+)/$', review_detail.as_view(), name='detail'),
#    url(r'^(?P\d+)/update$', review_update.as_view(), name='update'),
#    url(r'^(?P\d+)/delete$', review_delete.as_view(), name='delete'),
    )
