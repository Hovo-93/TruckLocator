from .models import Truck
from geopy.distance import geodesic


class CargoService:
    @staticmethod
    def get_nearby_trucks_count(pick_up_location):
        trucks = Truck.objects.all()
        count = 0
        for truck in trucks:
            truck_location = (
                truck.current_location.latitude,
                truck.current_location.longitude,
            )
            distance = geodesic(pick_up_location, truck_location).miles
            if distance <= 450:
                count += 1
        return count

    @staticmethod
    def get_nearby_trucks(pick_up_location):
        trucks = Truck.objects.all()
        nearby_trucks = []
        for truck in trucks:
            truck_location = (
                truck.current_location.latitude,
                truck.current_location.longitude,
            )
            distance = geodesic(pick_up_location, truck_location).miles
            if distance <= 450:
                truck_data = {
                    "truck_number": truck.number,
                    "distance_to_pick_up": distance,
                }
                nearby_trucks.append(truck_data)
        return nearby_trucks
