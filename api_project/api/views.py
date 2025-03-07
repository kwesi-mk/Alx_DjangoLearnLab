from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create your views here.
# class BookList(rest_framework.generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# class MyModelListCreateAPIView(generics.ListCreateAPIView):
#     queryset = MyModel.objects.all()
#     serializer_class = MyModelSerializer

#     def get_queryset(self):
#         queryset = self.queryset
#         name_filter = self.request.query_params.get('name', None)
#         if name_filter is not None:
#             queryset = queryset.filter(name__icontains=name_filter)
#             return queryset 