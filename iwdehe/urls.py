from django.conf.urls import patterns, include, url
from django.contrib import admin
from forum.views import *
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required



urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('haystack.urls'), name="search"),
    url(r'^$', 'sitio.views.home', name='nada'),
    url(r'^home/$', 'sitio.views.home', name='home'),
    url(r'^home/account/', include('allauth.urls')),
    url(r'^home/account/logout/', 'django.contrib.auth.views.logout', {'next_page': '/home/'}, name='logout'),
    url(r'^home/account/login/', 'django.contrib.auth.views.login', {'next_page': '/home/'}, name='login'),
    url(r'^restricted/', 'sitio.views.restricted', name='restricted'),
    url(r'^home/listreviews/$', review_listing.as_view(), name='listing'),
    url(r'^home/categorias/$', 'forum.views.categorias_listing', name='categorias'),
    url(r'^home/create/$', 'forum.views.review_create', name='create'),
    url(r'^home/categorias/add/$', permission_required('is_staff')(categoria_add.as_view()), name='categoria_add'),
    url(r'^cat_error/', 'forum.views.cat_error', name='cat_error'),
    url(r'^home/listreviews/(?P<pk>\d+)/$', 'forum.views.detail_review', name='detail'),
    url(r'^home/listreviews/comment/(?P<pk>\d+)/$', 'forum.views.comentar', name='comment'),
    url(r'^home/listreviews/denunciar/(?P<pk>\d+)/$', 'forum.views.denunciar', name='denunciar'),
    url(r'^home/(?P<pk>\d+)/update$', review_update.as_view(), name='update'),
    url(r'^home/(?P<pk>\d+)/delete$', review_delete.as_view(), name='delete'),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")),
    url(r'^home/userprofile$', 'sitio.views.userprofile', name='userprofile'),
    )

