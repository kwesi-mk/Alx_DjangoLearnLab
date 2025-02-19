from django.urls import path

from .views import list_books, LibraryDetailView

app_name = 'relationship_app'

urlpatterns = [
    path('', views.all_books, name='books'),
    path('', views.LibraryView.as_view(), name = 'library_view'),
]