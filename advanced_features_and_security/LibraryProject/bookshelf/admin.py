from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin 
from .models import CustomUser

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author',)

admin.site.register(Book, BookAdmin) 

class CustomUserAdmin(UserAdmin):
    """Admin panel customization for Customer"""
    model = CustomUser
    list_display = ("email", "first_name", "last_name", "date_of_birth", "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser", "date_of_birth")
    fieldsets = (
        (None, {"fields": ("email", "passwords")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ('wide',),
            "fields": ("email", "first_name", "last_name", "date_of_birth", "profile_photo", "password1", "password2", "is_staff", "is_superuser"),
        }),
    )
    search_fields = ("email","first_name", "last_name")
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)