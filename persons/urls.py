from django.conf.urls import patterns, url

from persons import views

urlpatterns = patterns('',
    url(r'^$', views.index , name="index"),
    url(r'^detail/(?P<id>\d+)/$', views.detail, name='detail'),
)