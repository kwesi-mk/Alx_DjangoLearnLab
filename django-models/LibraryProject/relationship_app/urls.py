from django.urls import path

from . import views

app_name = 'relationship_app'

urlpatterns = [
    path('', views.all_books, name='books'),
    path('', views.LibraryView.as_view(), name = 'library_view'),
]