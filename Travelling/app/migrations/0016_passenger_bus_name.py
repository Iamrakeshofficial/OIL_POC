# Generated by Django 4.0.3 on 2023-02-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_passenger_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='bus_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
