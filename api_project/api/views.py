from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# class BookList(rest_framework.generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return  True
        return request.user and request.user.is_staff 

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]



# class MyModelListCreateAPIView(generics.ListCreateAPIView):
#     queryset = MyModel.objects.all()
#     serializer_class = MyModelSerializer

#     def get_queryset(self):
#         queryset = self.queryset
#         name_filter = self.request.query_params.get('name', None)
#         if name_filter is not None:
#             queryset = queryset.filter(name__icontains=name_filter)
#             return queryset 


    
# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
    

