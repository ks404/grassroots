from api import read_from_csv
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Imports legislators into the database'

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        read_from_csv(options['path'])
        self.stdout.write(self.style.SUCCESS('Successfully imported representatives.'))
