# Generated by Django 5.1.7 on 2025-03-27 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0003_alter_useraccount_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='Date_Joined',
            field=models.DateField(default=datetime.datetime(2025, 3, 27, 8, 58, 34, 746021, tzinfo=datetime.timezone.utc)),
        ),
    ]
