from django.conf.urls import patterns, url

from lists import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'/todolist/^(?P<todolist_id>\d+)/', views.todolist, name='todolist')
)