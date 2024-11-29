# Generated by Django 3.0 on 2024-11-26 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp_app', '0021_auto_20241126_1908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='description',
            new_name='machineName',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='spare',
            new_name='sparePart',
        ),
        migrations.RemoveField(
            model_name='item',
            name='material',
        ),
        migrations.AddField(
            model_name='item',
            name='issuedqty',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='sparePartNo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]