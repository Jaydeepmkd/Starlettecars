# Generated by Django 4.2.2 on 2023-09-09 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0003_remove_booking_table_buss_vehicle_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='pass_reset_token',
            field=models.CharField(max_length=100, null=True),
        ),
    ]