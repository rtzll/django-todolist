from django.conf.urls import patterns, url

from accounts import views


urlpatterns = patterns('',
    url(r'^auth/login/', views.login_view, name='login'),
    url(r'^auth/logout/', views.logout_view, name='logout'),
)
