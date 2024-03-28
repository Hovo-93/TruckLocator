from random import random, randint
from random import choice
from faker import Faker
from truckLocator.models import Truck, Location

fake = Faker(["ru_RU"])


def generate_truck_fake_data(count):
    """
    Фейковые данные для Truck
    :param count:
    :return:
    """
    locations = Location.objects.all()[:400]
    for _ in range(count):
        random_location = choice(locations)

        truck_number = f"{randint(1000, 9999)}{choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
        carrying_capacity = randint(1, 1000)

        truck = Truck.objects.create(
            number=truck_number,
            current_location=random_location,
            carrying=carrying_capacity,
        )
        truck.save()
