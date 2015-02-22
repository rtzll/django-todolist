from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todolist.views.home', name='home'),
    url(r'^$', include('lists.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
