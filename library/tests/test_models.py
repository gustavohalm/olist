from django.test import TestCase
from library.models import Author, Book


def create_author(name):
    return Author.objects.create(name=name)


def create_book(name, edition, publication_year):
    return Book.objects.create(name=name, edition=edition, publication_year=publication_year)


class AuthorTest(TestCase):
    """
      Test for Author model
    """
    def test_create(self):
        author = create_author('Paulo de Tarso')
        self.assertEqual(author.name, author.__str__())


class BookTest(TestCase):
    """
      Test for Book model
    """

    def test_create(self):
        author = create_author('Moises')
        book = create_book('Numeros', '1', 1)
        book.authors.add(author)
        self.assertEqual(book.name, book.__str__())