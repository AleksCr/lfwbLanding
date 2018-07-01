from django.core.management.base import BaseCommand, CommandError
from stats_and_subscribe.models import Token
import logging


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        instance = Token.objects.all()
        instance.delete()
        logging.debug("table was cleaned")