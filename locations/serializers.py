from locations.models import Location
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'created_at', 'updated_at', 'name', 'latitude', 'longitude', 'number_of_spaces', 'parking_type', 'is_verified']