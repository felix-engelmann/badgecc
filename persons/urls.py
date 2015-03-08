from django.conf.urls import patterns, url

from persons import views

urlpatterns = patterns('',
    url(r'^$', views.index , name="index"),
)