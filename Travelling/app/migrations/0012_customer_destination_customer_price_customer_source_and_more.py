# Generated by Django 4.0.3 on 2023-02-06 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_customer_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='destination',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='source',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('Ticket_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Seat_no', models.CharField(max_length=10)),
                ('Date_of_journey', models.DateField()),
                ('Passenger_name', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('Booking_id', models.CharField(max_length=20)),
                ('Phone_number', models.CharField(max_length=15)),
                ('Bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.busdetails')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
