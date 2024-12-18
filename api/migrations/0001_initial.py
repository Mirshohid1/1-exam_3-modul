# Generated by Django 5.1.1 on 2024-12-12 10:30

import datetime
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(3)])),
                ('installed_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(1986, 1, 1)), django.core.validators.MaxValueValidator(datetime.date(2024, 12, 12))])),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(3)])),
                ('address', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(10)])),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(3)])),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1700), django.core.validators.MaxValueValidator(2024)])),
                ('vin', models.CharField(max_length=17, unique=True, validators=[django.core.validators.MinLengthValidator(17)])),
            ],
        ),
        migrations.CreateModel(
            name='SensorReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('timestamp', models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(1986, 1, 1, 12, 0)), django.core.validators.MaxValueValidator(datetime.datetime(2024, 12, 12, 10, 30, 9, 628243))])),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='api.sensor')),
            ],
        ),
        migrations.AddField(
            model_name='sensor',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to='api.vehicle'),
        ),
        migrations.CreateModel(
            name='MaintenanceSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(3)])),
                ('scheduled_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2024, 12, 12))])),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_schedules', to='api.vehicle')),
            ],
        ),
    ]
