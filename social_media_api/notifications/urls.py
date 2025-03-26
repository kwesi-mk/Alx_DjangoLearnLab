from django.urls import path
from posts.views import like_post
from notifications.views import user_notifications

urlpatterns += [
    path('notificatioins/', user_notifications, name='user-notifications'),
]