from django.core.management.base import BaseCommand
from django.utils import timezone

from budrys_app.models import Animals


class Command(BaseCommand):
    help = 'Deletes adopted Animals from database'

    def handle(self, *args, **options):
        now = timezone.now()
        Animals.objects.filter(updated_at__lt=now).delete()
