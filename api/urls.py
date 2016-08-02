from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'todolists', views.TodoListViewSet)
router.register(r'todos', views.TodoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
