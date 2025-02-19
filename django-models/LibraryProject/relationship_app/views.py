from django.shortcuts import render
from .models import Book
from .models import Library
from django.shortcuts import render, redirect  
from django.views.generic.detail import DetailView 
# Create your views here.

def all_books(request):
    books = Book.objects.all()


    return render(request, 'relationship_app/list_books.html', {
        'books' : books 
    })

class LibraryView(ListView):
    model = Library
    template =  'relationship_app/library_detail.html'


