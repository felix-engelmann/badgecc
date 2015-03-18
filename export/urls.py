from django.conf.urls import patterns, url

from export import views

urlpatterns = patterns('',
    url(r'^$', views.index , name="index"),
    url(r'^department/$', views.dep , name="department"),
    url(r'^updates/$', views.update , name="updates"),
)