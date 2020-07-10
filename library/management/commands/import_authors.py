from django.core.management.base import BaseCommand
from library.models import Author


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str, help='Path to Authors csv')

    def handle(self, *args, **options):
        csv = options['csv_path']
        with open(csv, 'r') as authors:
            for i, author in enumerate(authors.readlines()):
                if i < 0:
                    continue
                Author.objects.create(name=author.replace('\n', ''))