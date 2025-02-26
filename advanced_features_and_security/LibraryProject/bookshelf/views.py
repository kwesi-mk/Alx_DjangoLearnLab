from django.shortcuts import render
from django.contrib.auth.decorators import permission_required 
from django.shortcuts import render, get_object_or_404, redirect 
from django.db.models import Q 
from .models import Article 
from .models import Book 

# Create your views here.
@permission_required("relationship_app.can_view", raise_exception=True)
def article_list(request):
    """View all articles (only for users with can_view permission)"""
    articles = Article.objects.all()
    return render(request, "article_list.html", {"articles": articles})

@permission_required("relationship_app.can_create", raise_exception=True)
def article_create(request):
    """Create an article (only for users with can_create permission)"""
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Article.objects.create(title=title, content=content)
        return redirect("article_create.html")
    
@permission_required("relationship_app.can_edit", raise_exception=True)
def article_edit(request, article_id):
    """Edit an article (only for users with can_edit permission)"""
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()
        return redirect("article_list")
    return render(request, "article_edit.html", {"articlec": article})

@permission_required("relationship_app.can_delete", raise_exception=True)
def article_delete(request, article_id):
    """Delete an article (only for users with can_delete permission)"""
    article = get_object_or_404(Article, id=article_id)
    article.delete
    return redirect("article_list")

def book_list(request):
    """Secure book search implementation"""
    query = request.GET.get("q")
    if query:
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    else:
        books = Book.objects.all()
    return render(request, "relationship_app/list_book.html", {"books": books}) 