from django.shortcuts import render
from django_filters import rest_framework
from rest_framework import generics, permissions
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

# Create your views here.

class BookPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    
class CustomBookCreateView(generics.CreateAPIView):
    """Create a new book. Restricted to authenticated users."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Customize behaviour before saving the object."""
        serializers.save()

class CustomBookListView(generics.ListAPIView):
    """Retrieve all books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, filters.OrderingFilter]

    #Filtering
    filterset_fields = ['title', 'author', 'publication_year']

    #Searching
    search_fields = ['title', 'author']

    #Ordering
    #filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] #Default ordering

class CustomBookDetailView(generics.DetailAPIView):
    """Retrieves a single book by ID"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CustomBookUpdateView(generics.UpdateAPIView):
    """Update an existing book. Restricted to authenticated users."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """Customize behaviour before updating an object."""
        serializer.save()

class CustomBookDeleteView(generics.DestroyAPIView):
    """Delete a book. Restricted to authenticated users."""
    queryset = Book.objects.all()
    seriailizer_class = BookSerializer 
    permission_classes = [permissions.IsAuthenticated]