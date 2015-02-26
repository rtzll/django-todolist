from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'', include('lists.urls', namespace='lists')),
    url(r'^auth/', include('accounts.urls', namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),
)
