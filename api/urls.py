from django.conf.urls import url, include, patterns
from rest_framework import routers

from api import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'^todolists/$', views.todolists)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^todolists/$', views.todolists),
    url(r'^todolists/(?P<pk>[0-9]+)/$', views.todolist_detail),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
)