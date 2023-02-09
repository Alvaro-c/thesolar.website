# Generated by Django 4.1.5 on 2023-02-09 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('power', '0002_batteryvoltage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BatteryVoltage',
        ),
        migrations.AddField(
            model_name='result',
            name='battery_voltage',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
