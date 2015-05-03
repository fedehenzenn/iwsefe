from django.conf.urls import patterns, include, url
from django.contrib import admin
<<<<<<< HEAD
from forum.views import *
=======
from forum.views import review_create, review_update, review_listing, review_delete, detail_review
>>>>>>> 645e25f75bf84b03bf7ceb31c22bc8e6c4ad0f11


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
<<<<<<< HEAD
    url(r'^home/categorias/add/$', categoria_add.as_view(), name='categoria_add'),
    url(r'^home/listreviews/(?P<pk>\d+)/$', 'forum.views.detail_review', name='detail'),
    url(r'^home/listreviews/comment/(?P<pk>\d+)/$', 'forum.views.comentar', name='comment'),
=======
    url(r'^home/list/(?P<pk>\d+)/$', detail_review, name='detail'),
>>>>>>> 645e25f75bf84b03bf7ceb31c22bc8e6c4ad0f11
#    url(r'^(?P\d+)/update$', review_update.as_view(), name='update'),
#    url(r'^(?P\d+)/delete$', review_delete.as_view(), name='delete'),
    )
