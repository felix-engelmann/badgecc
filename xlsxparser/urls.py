from django.conf.urls import patterns, url

from xlsxparser import views

urlpatterns = patterns('',
    url(r'^$', views.index , name="index"),
)