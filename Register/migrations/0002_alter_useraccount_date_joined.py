# Generated by Django 5.1.7 on 2025-03-27 08:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='Date_Joined',
            field=models.DateField(default=datetime.datetime(2025, 3, 27, 8, 56, 0, 227314, tzinfo=datetime.timezone.utc)),
        ),
    ]
