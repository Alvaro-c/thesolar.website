from django.core.management import BaseCommand

from power.models import get_result


class Command(BaseCommand):
    help = "Gets one reading result from Arduino"

    def handle(self, *args, **options):
        get_result()
