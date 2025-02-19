from django.contrib import admin

from .models import Book, Library, Author, Librarian

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
