from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser 

from .models import Book, Library, Author, Librarian

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)



