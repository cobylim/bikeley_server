from django.contrib import admin
from .models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'parking_type', 'number_of_spaces', 'is_verified')
    list_filter = ['created_at', 'updated_at', 'is_verified', 'parking_type']

admin.site.register(Location, LocationAdmin)