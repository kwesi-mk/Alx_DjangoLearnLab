from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
 

from .views import list_books, LibraryDetailView, Admin_view, librarian_view, member_view 

app_name = 'relationship_app'

urlpatterns = [
    path('', views.all_books, name='books'),
    path('', views.LibraryView.as_view(), name = 'library_view'),
    path('register/', views.register, name='register'),
    #path('register/', SignUpView.as_view(template_name='relationship_app/register.html'), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-view/', Admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]