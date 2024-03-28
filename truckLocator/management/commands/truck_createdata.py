from django.core.management.base import BaseCommand

from truckLocator.generate_truck_fake_data import generate_truck_fake_data


class Command(BaseCommand):
    def handle(self, *args, **options):
        generate_truck_fake_data(20)
        print("Completed")
