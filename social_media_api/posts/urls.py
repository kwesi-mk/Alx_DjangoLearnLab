from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user_feed, like_post, unlike_post 

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('feed/', user_feed, name='user-feed'),
    path('<int:pk>/like/', like_post, name='like-post'),
    path('<int:pk>/unlike/', unlike_post, name='unlike-post'),
]