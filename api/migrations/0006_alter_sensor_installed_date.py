# Generated by Django 5.1.4 on 2024-12-12 22:36

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_sensorreading_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='installed_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(1986, 1, 1))]),
        ),
    ]
