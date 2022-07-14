from django.core.management.base import BaseCommand

from ...profile.utils import reset_today_score


class Command(BaseCommand):
    help = "reser_today_score"

    def handle(self, *args, **options):
        reset_today_score()