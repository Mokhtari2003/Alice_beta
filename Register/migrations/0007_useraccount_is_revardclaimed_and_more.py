# Generated by Django 5.1.7 on 2025-03-27 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0006_alter_useraccount_date_joined_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='is_RevardClaimed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='Date_Joined',
            field=models.DateField(default=datetime.datetime(2025, 3, 27, 9, 21, 23, 941148, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='Ref_Code',
            field=models.CharField(default='CRWOMT', max_length=6),
        ),
    ]
