# Generated by Django 4.0.3 on 2023-01-31 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_customer_gender_alter_customer_mobile_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='bus_name',
            field=models.CharField(default='Orange Tours and Travels', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default='Rakesh', max_length=30),
        ),
    ]
