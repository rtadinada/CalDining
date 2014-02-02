from django.conf.urls import patterns, url

from caleats import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^vote/$', views.vote),
    url(r'^favorite/$', views.favorite),
    url(r'^login/$', views._login),
    url(r'^logout/$', views._logout),
    url(r'^register/$', views._register),
    url(r'^(?P<hall>\S+)/$', views.detail, name='detail'),
)