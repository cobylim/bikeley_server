# Generated by Django 4.1.2 on 2022-12-03 20:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='is_verified',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='location',
            name='number_of_spaces',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='location',
            name='parking_type',
            field=models.CharField(blank=True, choices=[('BOLLARD', 'Bollard'), ('CORRAL', 'Corral'), ('DECORATIVE', 'Decorative'), ('GARAGE', 'Garage'), ('GRID', 'Grid'), ('HANDRAIL', 'Handrail'), ('HANGER', 'Hanger'), ('INNOVATIVE', 'Innovative'), ('LID', 'Lid'), ('LOCKER', 'Locker'), ('MINIMAL_FRONT', 'Minimal_front'), ('STAPLE', 'Staple'), ('WAVE', 'Wave'), ('PUMP_STATION', 'Pump Station'), ('REPAIR_STATION', 'Repair Station'), ('TREE', 'Tree'), ('RENTAL_STATION', 'Rental Station')], default=None, max_length=200),
        ),
    ]
