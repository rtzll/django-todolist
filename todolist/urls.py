from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # Django urls
    path("", include("lists.urls")),
    path("auth/", include("accounts.urls")),
    path("admin/", admin.site.urls),
    # JWT Token authentication urls
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # Other API urls
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
]
