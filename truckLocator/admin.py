from django.contrib import admin
from .models import *


class CargoInline(admin.TabularInline):
    model = Cargo
    fk_name = "pick_up_location"
    extra = 0


class TruckAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "current_location",
        "carrying",
    )


class LocationAdmin(admin.ModelAdmin):
    list_display = ("city", "state", "zip_code", "latitude", "longitude")
    inlines = [CargoInline]


class CargoAdmin(admin.ModelAdmin):
    list_display = ("pick_up_location", "delivery_location", "weight", "description")


admin.site.register(Truck, TruckAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Location, LocationAdmin)
