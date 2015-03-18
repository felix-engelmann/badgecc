from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'badges.views.home', name='home'),
    url(r'^$', include('persons.urls', namespace="persons")),
    url(r'^persons/', include('persons.urls', namespace="persons")),
    url(r'^export/', include('export.urls', namespace="export")),
    url(r'^parser/', include('xlsxparser.urls', namespace="parser")),

    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
