book_byAuthor = Book.objects.get(author = '')

books_inalibrary = Library.objects.get(books) 

librarian = Librarian.objects.get(library='')