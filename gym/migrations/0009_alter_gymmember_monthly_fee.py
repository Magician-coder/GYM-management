# Generated by Django 4.2.13 on 2024-08-17 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0008_gymmember_monthly_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymmember',
            name='monthly_fee',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
