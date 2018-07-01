from django.core.management.base import BaseCommand, CommandError
from stats_and_subscribe.models import Token
import logging


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        tokens_list = Token.objects.all()
        items = list(tokens_list.values_list('token', flat=True))
        # items = list(tokens_list.values_list())
        for s in items:
            logging.info(s)