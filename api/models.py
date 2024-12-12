from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from datetime import date, datetime


class Vehicle(models.Model):
    """
    The model representing the vehicle.
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

    def __str__(self):
        return f"Model: {self.model}, Year: {self.year}."


class Sensor(models.Model):
    """
    This model represents the fields of the car sensor.
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

    def __str__(self):
        return f"Sensor type: {self.type} for a vehicle: {self.vehicle.model}."
