from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from .models import Post
from .models import Comment 

# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
    
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Your username',
#         'class': 'w-full py-4 px-6 rounded-xl'
#     }))
#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         'placeholder': 'Your email address',
#         'class': 'w-full py-4 px-6 rounded-xl'
#     }))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'placeholder': 'Your password',
#         'class': 'w-full py-4 px-6 rounded-xl'
#     }))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'placeholder': 'Repeat password',
#         'class': 'w-full py-4 px-6 rounded-xl'
#     }))


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter tags seperated by commas.")
    class Meta:
        model = Post
        fields = ['title', 'content', 'TagWidget()']

    def save(self, commit=True):
        post = super().save(commit=False)
        tags = self.cleaned_data['tags']
        if commit:
            post.save()
            post.tags.set(*[tag.strip() for tag in tags.split(',') if tag])
        return post 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }