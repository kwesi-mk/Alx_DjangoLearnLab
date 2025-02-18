

book_byAuthor = Book.objects.get(author = '')



# list all books in a library 

books = Library.objects.get(name=library_name)
books.all()



librarian = Librarian.objects.get(library='')