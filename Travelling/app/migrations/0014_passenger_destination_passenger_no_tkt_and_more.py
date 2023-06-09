# Generated by Django 4.0.3 on 2023-02-07 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_customer_destination_alter_customer_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='destination',
            field=models.CharField(default='Odisha', max_length=20),
        ),
        migrations.AddField(
            model_name='passenger',
            name='no_tkt',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='passenger',
            name='price',
            field=models.IntegerField(default=2000),
        ),
        migrations.AddField(
            model_name='passenger',
            name='source',
            field=models.CharField(default='Hyderabad', max_length=20),
        ),
    ]
