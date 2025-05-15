from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenObtainPairView
)

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet, basename='post')
v1_router.register('groups', GroupViewSet, basename='group')
v1_router.register('follow', FollowViewSet, basename='followers')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

jwt_urlpatterns = [
    path('create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('verify/', TokenVerifyView.as_view(), name='jwt-verify'),
]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/jwt/', include(jwt_urlpatterns)),
]
