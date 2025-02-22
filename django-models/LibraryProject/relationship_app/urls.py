from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
 

from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view, add_book, edit_book, delete_book

app_name = 'relationship_app'

urlpatterns = [
    path("admin/", views.admin_view, name="admin-view"),
    path("librarian/", views.librarian_view, name="librarian-view"),
    path("member/", views.member_view, name="member-view"),
    path('', views.all_books, name='books'),
    path('', views.LibraryView.as_view(), name = 'library_view'),
    path('register/', views.register, name='register'),
    #path('register/', SignUpView.as_view(template_name='relationship_app/register.html'), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    
]