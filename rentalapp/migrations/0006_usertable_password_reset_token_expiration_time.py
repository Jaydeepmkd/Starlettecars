# Generated by Django 4.2.2 on 2023-10-04 20:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0005_rename_pass_reset_token_usertable_password_reset_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='password_reset_token_expiration_time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
