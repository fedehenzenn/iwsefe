from django.conf.urls import patterns, url
from .views import review_create, review_update, review_listing, review_delete, review_detail

urlpatterns = patterns('',
    url(r'^list/$', review_listing.as_view(), name='listing'),
    url(r'^create/$', review_create.as_view(), name='create'),
    url(r'^(?<pk>\d+)/$', review_detail.as_view(), name='detail'),
    url(r'^(?<pk>\d+)/update$', review_update.as_view(), name='update'),
    url(r'^(?<pk>\d+)/delete$', review_delete.as_view(), name='delete'),
    )