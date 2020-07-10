from django.test import TestCase
from library.models import Author, Book
from library.serializers import AuthorSerializer, BookSerializer


def create_author(name):
    return Author.objects.create(name=name)


def create_book(name, edition, publication_year):
    return Book.objects.create(name=name, edition=edition, publication_year=publication_year)


class AuthorSerializerTest(TestCase):
    """
      Test's for Author's serializing
    """
    def setUp(self):
        self.serializer_data = {
            'name': 'Salomao'
        }

        author = Author.objects.create(**self.serializer_data)
        self.serializer = AuthorSerializer(instance=author)

    def test_contains_field(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name']))

    def test_content(self):
        expected = {
            'name': 'Salomao'
        }
        self.assertEqual(self.serializer_data, expected)


class BookSerializerTest(TestCase):

    def setUp(self):

        author = create_author('Salomao')
        book = create_book(name='Salmos', edition='1', publication_year=1)
        book.authors.add(author)

        self.serializer = BookSerializer(instance=book)

    def test_contains_field(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'edition', 'publication_year', 'authors']))
