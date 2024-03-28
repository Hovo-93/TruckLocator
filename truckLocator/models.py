from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=255, verbose_name="город")
    state = models.CharField(max_length=255, verbose_name="штат")
    zip_code = models.CharField(
        max_length=10, unique=True, verbose_name="почтовый индекс"
    )
    latitude = models.FloatField(verbose_name="широта")
    longitude = models.FloatField(verbose_name="долгота")

    def __str__(self):
        return f"{self.city}, {self.state} {self.zip_code}"


class Cargo(models.Model):
    """
    Груз
    """

    pick_up_location = models.ForeignKey(
        Location, related_name="pick_up_location", on_delete=models.CASCADE
    )
    delivery_location = models.ForeignKey(
        Location, related_name="delivery_location", on_delete=models.CASCADE
    )
    weight = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        verbose_name="вес",
    )
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return f" from {self.pick_up_location} to {self.delivery_location}"


class Truck(models.Model):
    number = models.CharField(
        max_length=5, unique=True, verbose_name="уникальный номер"
    )
    current_location = models.ForeignKey(
        Location, on_delete=models.CASCADE, verbose_name="текущая локация"
    )
    carrying = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        verbose_name="грузоподъемность",
    )

    def __str__(self):
        return f"Truck {self.number}"
