# Generated by Django 4.0.3 on 2023-02-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_rename_seat_no_passenger_seatno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='driver_phono',
            field=models.CharField(max_length=12),
        ),
    ]
