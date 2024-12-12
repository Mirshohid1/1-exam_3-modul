from rest_framework.routers import DefaultRouter
from .models import Vehicle, Sensor, SensorReading, MaintenanceSchedule, ServiceCenter
from . import views

router = DefaultRouter()
router.register(r'Vehicles', views.VehicleViewSet)
router.register(r'Sensors', views.SensorViewSet)
router.register(r'SensorReadings', views.SensorReadingViewSet)
router.register(r'MaintenanceSchedules', views.MaintenanceScheduleViewSet)
router.register(r'ServiceCenters', views.ServiceCenterViewSet)

urlpatterns = router.urls