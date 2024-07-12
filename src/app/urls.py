from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path("", include("users.urls")),
    path(
        "docs/schema.yml",
        SpectacularAPIView.as_view(
            permission_classes=[IsAuthenticated, IsAdminUser],
            authentication_classes=[SessionAuthentication],
        ),
        name="schema",
    ),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema",
            permission_classes=[IsAuthenticated, IsAdminUser],
            authentication_classes=[SessionAuthentication],
        ),
        name="swagger-ui",
    ),
]
