from django.conf.urls import patterns, url

from accounts import views


urlpatterns = patterns('',
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
)
