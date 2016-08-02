from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'', include('lists.urls', namespace='lists')),
    url(r'^auth/', include('accounts.urls', namespace='auth')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
