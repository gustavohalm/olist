from django.core.management.base import BaseCommand
from library.models import Author


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str, help='Path to Authors csv')

    def handle(self, *args, **options):
        csv = options['csv_path']
        with open(csv, 'r') as lines:
            for i, line in enumerate(lines.readlines()):
                if i > 0:
                 Author.objects.create(name=line.replace('\n', ''))