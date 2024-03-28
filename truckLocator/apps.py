import time

import pandas as pd
from django.apps import AppConfig
from django.apps import apps as django_apps


class TrucklocatorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "truckLocator"

    def ready(self):
        Location = django_apps.get_model("truckLocator", "Location")

        if not Location.objects.exists():
            file_path = "uszips.csv"

            df = pd.read_csv(file_path)
            data = df.to_dict("records")
            Location.objects.bulk_create(
                [
                    Location(
                        city=row["city"],
                        state=row["state_name"],
                        zip_code=row["zip"],
                        latitude=row["lat"],
                        longitude=row["lng"],
                    )
                    for row in data
                ]
            )
