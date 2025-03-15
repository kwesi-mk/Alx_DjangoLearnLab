from django.db import models

# Create your models here.
# The author model that gets only the name of the author.
class Author(models.Model):
    name = models.CharField(max_length=30)


# The book model that gets the title, publication and author of a book.
class Book(models.Model):
    title = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
