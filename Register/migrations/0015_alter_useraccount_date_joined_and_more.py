# Generated by Django 5.1.7 on 2025-04-10 12:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0014_alter_useraccount_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='Date_Joined',
            field=models.DateField(default=datetime.datetime(2025, 4, 10, 12, 18, 32, 685607, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='Ref_Code',
            field=models.CharField(default='NAN237EKRU', max_length=10),
        ),
    ]
