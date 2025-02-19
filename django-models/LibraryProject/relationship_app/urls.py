from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views 

from .views import list_books, LibraryDetailView

app_name = 'relationship_app'

urlpatterns = [
    path('', views.all_books, name='books'),
    path('', views.LibraryView.as_view(), name = 'library_view'),
    path('register/', views.register, name='register'),
    #path('register/', SignUpView.as_view(template_name='relationship_app/register.html'), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout')
]