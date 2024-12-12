from rest_framework.viewsets import ModelViewSet
from .models import Vehicle, Sensor, SensorReading, MaintenanceSchedule, ServiceCenter
from .serializers import (
    VehicleSerializer, VehicleInputSerializer,
    SensorSerializer, SensorInputSerializer,
    SensorReadingSerializer, SensorReadingInputSerializer,
    MaintenanceScheduleSerializer, MaintenanceScheduleInputSerializer,
    ServiceCenterSerializer, ServiceCenterInputSerializer,
)


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return VehicleInputSerializer
        return VehicleSerializer


class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return SensorInputSerializer
        return SensorSerializer


class SensorReadingViewSet(ModelViewSet):
    queryset = SensorReading.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return SensorReadingInputSerializer
        return SensorReadingSerializer


class MaintenanceScheduleViewSet(ModelViewSet):
    queryset = MaintenanceSchedule.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return MaintenanceScheduleInputSerializer
        return MaintenanceScheduleSerializer


class ServiceCenterViewSet(ModelViewSet):
    queryset = ServiceCenter.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ServiceCenterInputSerializer
        return ServiceCenterSerializer