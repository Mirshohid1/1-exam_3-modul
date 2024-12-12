from rest_framework import serializers
from .models import Vehicle, Sensor, SensorReading, MaintenanceSchedule, ServiceCenter


# Vehicle
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'model', 'year', 'vin']


class VehicleInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['model', 'year', 'vin']


# Sensor
class SensorSerializer(serializers.ModelSerializer):
    vehicle_id = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all(), source='vehicle')

    class Meta:
        model = Sensor
        fields = ['id', 'type', 'vehicle_id', 'installed_date']


class SensorInputSerializer(serializers.ModelSerializer):
    vehicle_id = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all(), source='vehicle')

    class Meta:
        model = Sensor
        fields = ['type', 'vehicle_id', 'installed_date']


# SensorReading
class SensorReadingSerializer(serializers.ModelSerializer):
    sensor_id = serializers.PrimaryKeyRelatedField(queryset=Sensor.objects.all(), source='sensor')

    class Meta:
        model = SensorReading
        fields = ['id', 'sensor_id', 'value', 'timestamp']


class SensorReadingInputSerializer(serializers.ModelSerializer):
    sensor_id = serializers.PrimaryKeyRelatedField(queryset=Sensor.objects.all(), source='sensor')

    class Meta:
        model = SensorReading
        fields = ['sensor_id', 'value', 'timestamp']


# MaintenanceSchedule
class MaintenanceScheduleSerializer(serializers.ModelSerializer):
    vehicle_id = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all(), source='vehicle')

    class Meta:
        model = MaintenanceSchedule
        fields = ['id', 'vehicle_id', 'service_type', 'scheduled_date']


class MaintenanceScheduleInputSerializer(serializers.ModelSerializer):
    vehicle_id = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all(), source='vehicle')

    class Meta:
        model = MaintenanceSchedule
        fields = ['vehicle_id', 'service_type', 'scheduled_date']


# ServiceCenter
class ServiceCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCenter
        fields = ['id', 'name', 'address', 'rating']


class ServiceCenterInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCenter
        fields = ['name', 'address', 'rating']