from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from app.api.user import views as user_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('app.api.urls')),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Authorization
    path('api/auth/register/', user_views.UserViewSet.as_view({'post': 'create_user'}), name='user_create'),
    path('api/auth/me/', user_views.UserViewSet.as_view({'get': 'current_user'}), name='current_user'),
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/auth/jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
]
