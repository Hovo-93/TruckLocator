from rest_framework import status
from rest_framework.response import Response
from .models import Cargo, Location, Truck
from .serializers import (
    CargoSerializer,
    TruckSerializer,
    CargoUpdateSerializer,
    CargoDetailSerializer,
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
)


class CargoCreateView(CreateAPIView):
    """
    Создание нового груза
    """
    serializer_class = CargoSerializer

    def create(self, request, *args, **kwargs):
        # pick_up_zip = request.body.get("pick_up_location.zip_code")
        pick_up_zip = request.data.get("pick_up_location")
        print(pick_up_zip)
        delivery_zip = request.data.get("delivery_location")
        print(delivery_zip)
        weight = request.data.get("weight")
        description = request.data.get("description")

        try:
            pick_up_location = Location.objects.get(zip_code=pick_up_zip)
            delivery_location = Location.objects.get(zip_code=delivery_zip)

            cargo = Cargo(
                pick_up_location=pick_up_location,
                delivery_location=delivery_location,
                weight=weight,
                description=description,
            )

            cargo.save()

            serializer = CargoSerializer(cargo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Location.DoesNotExist:
            return Response(
                {"error": "One or both zip codes are invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class CargoListView(ListAPIView):
    """
    Получение списка грузов
    """
    serializer_class = CargoSerializer
    queryset = Cargo.objects.all()


class TruckUpdateView(RetrieveUpdateAPIView):
    """
    Редактирование машины
    """
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    lookup_field = "number"

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        zip_code = data.get("current_location", None)
        if zip_code:
            try:
                # Поиск локации по zip-коду
                location = Location.objects.get(zip_code=zip_code)
                instance.current_location = location
                instance.save()
            except Location.DoesNotExist:
                return Response(
                    {"error": "Location with this zip code does not exist"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class CargoUpdateView(UpdateAPIView):
    """
    Редактирование груза по ID
    """
    serializer_class = CargoUpdateSerializer
    queryset = Cargo.objects.all()
    lookup_field = "pk"

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        if "weight" in request.data:
            instance.weight = request.data["weight"]
        if "description" in request.data:
            instance.description = request.data["description"]

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.partial_update(serializer)

        return Response(serializer.data)


class CargoDeleteView(DestroyAPIView):
    """
    Удаление груза по ID
    """
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": f"Cargo {instance} deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class CargoDetailView(RetrieveAPIView):
    """
    Получение информации о конкретном грузе по ID
    """
    queryset = Cargo.objects.all()
    serializer_class = CargoDetailSerializer
    lookup_field = "id"
