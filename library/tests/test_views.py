from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from library.models import Author, Book

mock_authors = [
    {'name': 'Bruce Anstey'},
    {'name': 'John Nelson Darby'},
    {'name': 'Mairo Persona'},
    {'name': 'delete me'}
]

mock_books = [
    {
        'name': 'Book A',
        'edition': 'Edition 1',
        'publication_year': 2004,
        'authors_id': [
            1,
            2
        ]
    },
    {
        'name': 'Book B',
        'edition': 'Edition 1',
        'publication_year': 2014,
        'authors_id': [
            2,
            3
        ]
    },
    {
        'name': 'Book C',
        'edition': 'Edition 3',
        'publication_year': 2004,
        'authors_id': [
            1
        ]
    }
]


def create_mocks():
    for author in mock_authors:
        Author.objects.create(name=author['name'])

    for book in mock_books:
        created_book = Book.objects.create(name=book['name'], edition=book, publication_year=book['publication_year'])
        for author_id in book['authors_id']:
            created_book.authors.add(Author.objects.get(pk=author_id))


class AuthorViewSetTest(TestCase):
    """
      Test's for Author's endpoint
    """

    def setUp(self):
        self.url = '/api/authors/'
        self.client = APIClient()
        create_mocks()

    def test_create(self):
        res = self.client.post(self.url, {'name': 'Davi'}, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_list_with_name(self):
        res = self.client.get(self.url, {'name': 'Bruce Anstey'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json()['results'][0]['name'], 'Bruce Anstey')

    def test_update(self):
        res = self.client.put(self.url+'3', {'name': 'Mario Persona'}, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json()['name'], 'Mario Persona')

    def test_delete(self):
        res = self.client.delete(self.url+'4')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)


class BookViewSetTest(TestCase):
    """
      Test's for Book's endpoint
    """

    def setUp(self):
        self.url = '/api/books/'
        self.client = APIClient()
        create_mocks()

    def test_create(self):
        data = {
            'name': 'Book created',
            'edition': '0.1',
            'publication_year': 2020,
            'authors_id': [
                1
            ]
        }
        res = self.client.post(self.url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_list_with_params(self):
        res = self.client.get(self.url, {'publication_year': 2004})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json()['results'][0]['publication_year'], 2004)

    def test_update(self):
        data = {
            'name': 'Updating a Book',
            'edition': '0.02',
            'publication_year': 2004,
            'authors_id': [
                1,
                2,
                3
            ]
        }
        res = self.client.put(self.url+'1', data, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json()['name'], 'Updating a Book')

    def test_delete(self):
        res = self.client.delete(self.url+'3')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
