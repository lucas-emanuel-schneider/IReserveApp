from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path(
        'api/v1/token/refresh/',
        TokenRefreshView.as_view(), name='token_refresh'),
    path(
        'api/v1/token/verify/',
        TokenVerifyView.as_view(), name='token_verify'),
    path("api/v1/", include("api.urls")),
]
