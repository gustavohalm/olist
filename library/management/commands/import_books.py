from django.core.management.base import BaseCommand
from library.models import Book, Author


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str, help='Path to Books csv')

    def handle(self, *args, **options):
        csv = options['csv_path']
        with open(csv, 'r') as books:
            for i, book in enumerate(books.readlines()):
                if i == 0:
                    continue
                name, edition, publication_year, authors_id = book.replace('\n', '').split(',')
                imported_book = Book.objects.create(name=name, edition=edition, publication_year=publication_year)
                for author_id in authors_id.split('-'):
                    imported_book.authors.add(Author.objects.get(pk=author_id))
