# Generated by Django 3.0 on 2024-11-27 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp_app', '0025_auto_20241127_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocktodept',
            name='date',
            field=models.DateField(null=True),
        ),
    ]