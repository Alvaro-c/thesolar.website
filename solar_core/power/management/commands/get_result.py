from django.core.management import BaseCommand

from power.models import Result


class Command(BaseCommand):
    help = "Gets one reading result from Arduino"

    def handle(self, *args, **options):
        Result.get_result()
