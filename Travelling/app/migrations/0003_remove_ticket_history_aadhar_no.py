# Generated by Django 4.0.3 on 2023-01-30 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_newuser_mobile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket_history',
            name='aadhar_no',
        ),
    ]