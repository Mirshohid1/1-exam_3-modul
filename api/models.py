from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from datetime import date


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