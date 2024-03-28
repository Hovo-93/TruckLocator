from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CargoCreateView,
    CargoListView,
    TruckUpdateView,
    CargoUpdateView,
    CargoDeleteView,
    CargoDetailView,
)


urlpatterns = [
    path("cargo/list/", CargoListView.as_view(), name="cargo-list"),
    path("cargo/create/", CargoCreateView.as_view(), name="cargo-create"),
    path("cargo/update/<int:pk>/", CargoUpdateView.as_view(), name="cargo-update"),
    path("cargo/delete/<int:id>/", CargoDeleteView.as_view(), name="cargo-delete"),
    path("cargo/detail/<int:id>/", CargoDetailView.as_view(), name="cargo-detail"),
    path("truck/<str:number>/", TruckUpdateView.as_view(), name="truck-update"),
]
