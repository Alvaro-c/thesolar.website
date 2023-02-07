from django.core.management import BaseCommand

from solar_core.power.models import Result


class Command(BaseCommand):
    help = "Gets one reading result from Arduino"

    def handle(self, *args, **options):
        Result.get_result()

