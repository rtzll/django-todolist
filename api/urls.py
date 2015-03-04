from django.conf.urls import url, include, patterns

from api import views


urlpatterns = patterns('',
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^todolists/$', views.TodoLists.as_view()),
    url(r'^todolists/(?P<pk>[0-9]+)/$', views.TodoListDetail.as_view()),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
)
