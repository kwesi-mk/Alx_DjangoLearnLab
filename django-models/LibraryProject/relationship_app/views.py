from django.shortcuts import render, get_object_or_404, redirect 
from .models import Book
from .models import Library
from .models import UserProfile 
from django.shortcuts import render, redirect  
from django.views.generic.detail import DetailView 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy 
from django.contrib.auth.decorators import user_passes_test, login_required  
from .forms import BookForm
from django.contrib.auth.decorators import permission_required
# Create your views here.

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


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

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app/can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/confirm_delete.html', {'book':book})









# def is_admin(user):
#     return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# def is_librarian(user):
#     return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# def is_member(user):
#     return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# #Admin view
# @login_required
# @user_passes_test(is_admin)
# def admin_view(request):
#     return render(request, "relationship_app/admin_view.html", {"role":"Admin"})

# #Librarian View
# @login_required
# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, "relationship_app/librarian_view.html", {"role": "Librarian"})
    
# #Member View
# @login_required
# @user_passes_test(is_member)
# def member_view(request):
#     return render(request, "relationship_app/member_view.html", {"role":"Member"})
