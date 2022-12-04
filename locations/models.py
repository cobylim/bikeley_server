from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Location(models.Model):
    BOLLARD = 'BOLLARD'
    CORRAL = 'CORRAL'
    DECORATIVE = 'DECORATIVE'
    GARAGE = 'GARAGE'
    GRID = 'GRID'
    HANDRAIL = 'HANDRAIL'
    HANGER = 'HANGER'
    INNOVATIVE = 'INNOVATIVE'
    LID = 'LID'
    LOCKER = 'LOCKER'
    MINIMAL_FRONT = 'MINIMAL_FRONT'
    STAPLE = 'STAPLE'
    WAVE = 'WAVE'
    PUMP_STATION = 'PUMP_STATION'
    REPAIR_STATION = 'REPAIR_STATION'
    TREE = 'TREE'
    RENTAL_STATION = 'RENTAL_STATION'

    PARKING_TYPE_CHOICES = [
        (BOLLARD, 'Bollard'),
        (CORRAL, 'Corral'),
        (DECORATIVE, 'Decorative'),
        (GARAGE, 'Garage'),
        (GRID, 'Grid'),
        (HANDRAIL, 'Handrail'),
        (HANGER, 'Hanger'),
        (INNOVATIVE, 'Innovative'),
        (LID, 'Lid'),
        (LOCKER, 'Locker'),
        (MINIMAL_FRONT, 'Minimal_front'),
        (STAPLE, 'Staple'),
        (WAVE, 'Wave'),
        (PUMP_STATION, 'Pump Station'),
        (REPAIR_STATION, 'Repair Station'),
        (TREE, 'Tree'),
        (RENTAL_STATION, 'Rental Station'),
    ]

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    name = models.CharField(max_length=200, blank=True, default='')
    number_of_spaces = models.IntegerField(blank=True, null=True)
    parking_type = models.CharField(max_length=200, choices=PARKING_TYPE_CHOICES, blank=True, default='')
    is_verified = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.name
