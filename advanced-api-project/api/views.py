from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated 

# Create your views here.
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