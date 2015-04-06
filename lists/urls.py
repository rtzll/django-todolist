from django.conf.urls import patterns, url

from lists import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^todolist/(?P<todolist_id>\d+)/$', views.todolist, name='todolist'),
    url(r'^todolist/new/$', views.new_todolist, name='new_todolist'),
    url(r'^todolist/add/$', views.add_todolist, name='add_todolist'),
    url(r'^todolists/$', views.overview, name='overview'),
)
