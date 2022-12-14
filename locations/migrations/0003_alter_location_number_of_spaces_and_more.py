# Generated by Django 4.1.2 on 2022-12-03 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_location_created_at_location_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='number_of_spaces',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='parking_type',
            field=models.CharField(blank=True, choices=[('BOLLARD', 'Bollard'), ('CORRAL', 'Corral'), ('DECORATIVE', 'Decorative'), ('GARAGE', 'Garage'), ('GRID', 'Grid'), ('HANDRAIL', 'Handrail'), ('HANGER', 'Hanger'), ('INNOVATIVE', 'Innovative'), ('LID', 'Lid'), ('LOCKER', 'Locker'), ('MINIMAL_FRONT', 'Minimal_front'), ('STAPLE', 'Staple'), ('WAVE', 'Wave'), ('PUMP_STATION', 'Pump Station'), ('REPAIR_STATION', 'Repair Station'), ('TREE', 'Tree'), ('RENTAL_STATION', 'Rental Station')], default='', max_length=200),
        ),
    ]
