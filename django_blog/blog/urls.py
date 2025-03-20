from django.contrib.auth.views import LoginView, LogoutView 
from django.urls import path
from . import views 
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView, search_posts, posts_by_tag
#from .views import register 


app_name = 'blog'

# urlpatterns = [
#     #path('', views.home, name='home'),
#     path('', views.index, name='index'),
#     path('home/', views.home, name='home'),
#     path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
#     path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
#     path('register/', views.register, name='register'),
# ]

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:comment_id>/update/', CommentUpdateView.as_view(), name='edit-comment'),
    path('comment/<int:comment_id>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
    path('search/', search_posts, name='search-posts'),
    path('tags/<slug:tag_slug>/', posts_by_tag, name='posts-by-tag'),

]