from django.conf.urls import url, include, patterns

from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'todolists', views.TodoListViewSet)
router.register(r'todos', views.TodoViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
