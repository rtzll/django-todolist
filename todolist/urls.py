from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('lists.urls')),
    path('auth/', include('accounts.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
