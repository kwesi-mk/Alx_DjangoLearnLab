from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        #Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        #Create sample books
        self.book1 = Book.objects.create(title='Book One', author='Author One', publication_year=2000)
        self.book2 = Book.objects.create(title='Book Two', author='Author Two', publication_year=2010)

        #Authenticate the user
        self.client.login(username='testuser', password='testpassword')

    def test_get_books_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_create_book(self):
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2022}
        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        data = {'title': 'Updated Book', 'author': 'Updated Author', 'publication_year' : 2025}
        response = self.client.put(f'/api/books/{self.book1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        response = self.client.get('/api/books/?author=Author One')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_search_books_by_title(self):
        response = self.client.get('/api/books/?search=Book One')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_order_books_by_year(self):
        response = self.client.get('/api/books/?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['publication_year'], 2000) 