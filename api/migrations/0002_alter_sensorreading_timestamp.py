# Generated by Django 5.1.1 on 2024-12-12 16:57

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorreading',
            name='timestamp',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(1986, 1, 1, 12, 0, tzinfo=datetime.timezone.utc)), django.core.validators.MaxValueValidator(datetime.datetime(2024, 12, 12, 16, 57, 35, 112545, tzinfo=datetime.timezone.utc))]),
        ),
    ]
