# Generated by Django 3.0 on 2024-11-27 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp_app', '0026_stocktodept_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepttoDept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machineName', models.CharField(max_length=500, null=True)),
                ('sparePart', models.CharField(max_length=500, null=True)),
                ('sparePartNo', models.CharField(max_length=500, null=True)),
                ('qty', models.IntegerField(max_length=500, null=True)),
                ('fromdepartment', models.CharField(max_length=500, null=True)),
                ('todepartment', models.CharField(max_length=500, null=True)),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]