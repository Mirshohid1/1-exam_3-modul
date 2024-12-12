from rest_framework.viewsets import ModelViewSet

from .models import Vehicle, Sensor, SensorReading, MaintenanceSchedule, ServiceCenter
from .serializers import (
    VehicleSerializer, VehicleInputSerializer,
    SensorSerializer, SensorInputSerializer,
    SensorReadingSerializer, SensorReadingInputSerializer,
    MaintenanceScheduleSerializer, MaintenanceScheduleInputSerializer,
    ServiceCenterSerializer, ServiceCenterInputSerializer,
)
from .utils import create_schema_view


@create_schema_view(
    model_name="Avtomobil",
    plural_name="avtomobillar",
    tag_name="vehicles",
    input_serializer=VehicleInputSerializer,
    output_serializer=VehicleSerializer,
)
class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return VehicleInputSerializer
        return VehicleSerializer


@create_schema_view(
    model_name="Sensor",
    plural_name="sensorlar",
    tag_name="sensors",
    input_serializer=SensorInputSerializer,
    output_serializer=SensorSerializer,
)
class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return SensorInputSerializer
        return SensorSerializer


@create_schema_view(
    model_name="SensorReading",
    plural_name="sensor readinglar",
    tag_name="sensor readings",
    input_serializer=SensorReadingInputSerializer,
    output_serializer=SensorReadingSerializer,
)
class SensorReadingViewSet(ModelViewSet):
    queryset = SensorReading.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return SensorReadingInputSerializer
        return SensorReadingSerializer


@create_schema_view(
    model_name="MaintenanceSchedule",
    plural_name="texnik xizmatlar",
    tag_name="maintenance",
    input_serializer=MaintenanceScheduleInputSerializer,
    output_serializer=MaintenanceScheduleSerializer,
)
class MaintenanceScheduleViewSet(ModelViewSet):
    queryset = MaintenanceSchedule.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return MaintenanceScheduleInputSerializer
        return MaintenanceScheduleSerializer


@create_schema_view(
    model_name="ServiceCenter",
    plural_name="servis markazlari",
    tag_name="service_centers",
    input_serializer=ServiceCenterInputSerializer,
    output_serializer=ServiceCenterSerializer,
)
class ServiceCenterViewSet(ModelViewSet):
    queryset = ServiceCenter.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ServiceCenterInputSerializer
        return ServiceCenterSerializer