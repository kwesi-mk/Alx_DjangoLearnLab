from django.shortcuts import render
from .models import Book
from .models import Library
from .models import UserProfile
from django.shortcuts import render, redirect  
from django.views.generic.detail import DetailView 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy 
from django.contrib.auth.decorators import user_passes_test 
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {
        'form': form
    })
#class SignUpView(CreateView):
#    form_class = UserCreationForm
#    success_url = reverse_lazy('login')
#    template_name = 'relationship_app/register.html'
def list_books(request):
    books = Book.objects.all()


    return render(request, 'relationship_app/list_books.html', {
        'books' : books 
    })

class LibraryDetailView(DetailView):
    model = Library
    template =  'relationship_app/library_detail.html'


def is_admin(user):
    return user.UserProfile.role == 'Admin'

def is_librarian(user):
    return user.UserProfile.role == 'Librarian'

def is_member(user):
    return user.UserProfile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')


