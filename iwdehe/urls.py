from django.conf.urls import patterns, include, url
from django.contrib import admin
from forum.views import *



urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'sitio.views.home', name='nada'),
    url(r'^home/$', 'sitio.views.home', name='home'),
    url(r'^home/account/', include('allauth.urls')),
    url(r'^home/account/logout/', 'django.contrib.auth.views.logout', {'next_page': '/home/'}, name='logout'),
    url(r'^home/account/login/', 'django.contrib.auth.views.login', {'next_page': '/home/'}, name='login'),
    url(r'^restricted/', 'sitio.views.restricted', name='restricted'),
    url(r'^home/listreviews/$', review_listing.as_view(), name='listing'),
    url(r'^home/categorias/$', 'forum.views.categorias_listing', name='categorias'),
    url(r'^home/create/$', review_create.as_view(), name='create'),
    url(r'^home/categorias/add/$', categoria_add.as_view(), name='categoria_add'),
    url(r'^home/listreviews/(?P<pk>\d+)/$', 'forum.views.detail_review', name='detail'),
    url(r'^home/listreviews/comment/(?P<pk>\d+)/$', 'forum.views.comentar', name='comment'),
    url(r'^home/listreviews/denunciar/(?P<pk>\d+)/$', 'forum.views.denunciar', name='denunciar'),
    url(r'^home/(?P<pk>\d+)/update$', review_update.as_view(), name='update'),
    url(r'^home/(?P<pk>\d+)/delete$', review_delete.as_view(), name='delete'),
    )
