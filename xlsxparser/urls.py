from django.conf.urls import patterns, url

from xlsxparser import views

urlpatterns = patterns('',
    url(r'^$', views.index , name="index"),
    url(r'^images/$', views.images , name="images"),
    url(r'^insert/$', views.insert , name="insert"),
    url(r'^manual/$', views.manual , name="manual"),
    url(r'^upload/$', views.upload , name="upload"),
)