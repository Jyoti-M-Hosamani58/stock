# Generated by Django 3.0 on 2024-11-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp_app', '0027_depttodept'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deptstock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machineName', models.CharField(max_length=500, null=True)),
                ('sparePart', models.CharField(max_length=500, null=True)),
                ('sparePartNo', models.CharField(max_length=500, null=True)),
                ('qty', models.IntegerField(max_length=500, null=True)),
                ('department', models.CharField(max_length=500, null=True)),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]
