from rest_framework_simplejwt.views import (
        TokenRefreshView,
    )
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, token, reg_user_email


urlpatterns = [
    path('v1/auth/token/refresh/', TokenRefreshView.as_view(),
        name='token_refresh'),
    path('v1/auth/token/email/', reg_user_email),
    path('v1/auth/token/', token),

    ]
router = DefaultRouter()
# router.register(r'users/me',
#     UserViewSet, basename='api_users_me')
router.register(r'users',
    UserViewSet, basename='api_users')
urlpatterns += [
    path('v1/', include(router.urls)),
    ]
