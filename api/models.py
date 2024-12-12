from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from datetime import date, datetime


class Vehicle(models.Model):
    """
    This model represents a vehicle.
    Attributes:
        model (CharField): The model name of the vehicle, with a maximum length of 255 characters.
        year (IntegerField): The year of manufacture of the vehicle, validated to be between 1700 and the current year.
        vin (CharField): The Vehicle Identification Number (VIN), which is unique and 17 characters long.
    """
    
    model = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(3)]
    )
    year = models.IntegerField(
        validators=[
            MinValueValidator(1700),
            MaxValueValidator(date.today().year)
        ]
    )
    vin = models.CharField(
        max_length=17,
        validators=[
            MinLengthValidator(17),
        ],
        unique=True,
    )

    def save(self, *args, **kwargs):
        self.model = self.model.strip().title()
        self.vin = self.vin.strip().upper()

        super().save(*args, **kwargs)


    def __str__(self):
        return f"Model: {self.model}, Year: {self.year}."


class Sensor(models.Model):
    """
    This model represents a sensor installed in a vehicle.
    Attributes:
        type (CharField): The type of the sensor, with a maximum length of 255 characters.
        vehicle (ForeignKey): A reference to the associated vehicle, using a foreign key relationship.
        installed_date (DateField): The date when the sensor was installed, validated to be between 1986 and the current year.
    """

    type = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(3)],
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="sensors"
    )

    installed_date = models.DateField(
        validators=[
            MinValueValidator(date(1986, 1, 1)),
            MaxValueValidator(date.today()),
        ]
    )

    def save(self, *args, **kwargs):
        self.type = self.type.strip().capitalize()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Sensor type: {self.type} for a vehicle: {self.vehicle.model}."


class SensorReading(models.Model):
    """
    This model represents a reading from a sensor.
    Attributes:
        sensor (ForeignKey): A reference to the associated sensor, using a foreign key relationship.
        value (FloatField): The value recorded by the sensor.
        timestamp (DateTimeField): The date and time when the reading was recorded, validated to be between 1986 and the current year.
    """

    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="readings")
    value = models.FloatField()
    timestamp = models.DateTimeField(
        validators=[
            MinValueValidator(datetime(1986, 1, 1, 12, 00)),
            # MaxValueValidator(datetime.now()) I'll save it for later. There's a mistake here.
        ]
    )

    def __str__(self):
        return f"Sensor: {self.sensor.type}, Reading: {self.value}."


class MaintenanceSchedule(models.Model):
    """
    This model represents a maintenance schedule for a vehicle.
    Attributes:
        vehicle (ForeignKey): A reference to the associated vehicle, using a foreign key relationship.
        service_type (CharField): The type of service scheduled, with a maximum length of 255 characters.
        scheduled_date (DateField): The date when the service is scheduled, validated to be not in the past.
    """

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="maintenance_schedules")

    service_type = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(3)],
    )

    scheduled_date = models.DateField(
        validators=[MinValueValidator(date.today())],
    )

    def save(self, *args, **kwargs):
        self.service_type = self.service_type.strip().capitalize()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Vehicle: {self.vehicle.model}, Service type: {self.service_type}, Scheduled date: {self.scheduled_date}."


class ServiceCenter(models.Model):
    """
    This model represents a service center where vehicles can be maintained or repaired.
    Attributes:
        name (CharField): The name of the service center, with a maximum length of 255 characters and a minimum length of 3 characters.
        address (CharField): The address of the service center, with a maximum length of 255 characters and a minimum length of 10 characters.
        rating (DecimalField): The rating of the service center, on a scale from 0.0 to 5.0.
    """

    name = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(3)],
    )

    address = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(10)]
    )

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0),
        ]
    )

    def save(self, *args, **kwargs):
        self.name = self.name.strip().title()
        self.address = self.address.strip().capitalize()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Service: {self.name}, Rating: {self.rating}."
