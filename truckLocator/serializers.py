from rest_framework import serializers
from .models import Truck, Location, Cargo
from .services import CargoService


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("zip_code",)


class TruckSerializer(serializers.ModelSerializer):
    current_location = LocationSerializer(read_only=True)

    class Meta:
        model = Truck
        fields = ("number", "current_location", "carrying")


class CargoSerializer(serializers.ModelSerializer):
    pick_up_location = LocationSerializer()
    delivery_location = LocationSerializer()
    nearby_trucks_count = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = (
            "id",
            "pick_up_location",
            "delivery_location",
            "weight",
            "description",
            "nearby_trucks_count",
        )

    def get_nearby_trucks_count(self, obj):
        pick_up_location = (
            obj.pick_up_location.latitude,
            obj.pick_up_location.longitude,
        )
        return CargoService.get_nearby_trucks_count(pick_up_location)


class CargoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ("id", "weight", "description")


class CargoDetailSerializer(serializers.ModelSerializer):
    pick_up_location = LocationSerializer()
    delivery_location = LocationSerializer()
    nearby_trucks = serializers.SerializerMethodField()
    nearby_trucks_count = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = (
            "id",
            "pick_up_location",
            "delivery_location",
            "weight",
            "description",
            "nearby_trucks_count",
            "nearby_trucks",
        )

    def get_nearby_trucks(self, obj):
        pick_up_location = (
            obj.pick_up_location.latitude,
            obj.pick_up_location.longitude,
        )
        return CargoService.get_nearby_trucks(pick_up_location)

    def get_nearby_trucks_count(self, obj):
        pick_up_location = (
            obj.pick_up_location.latitude,
            obj.pick_up_location.longitude,
        )
        return CargoService.get_nearby_trucks_count(pick_up_location)
