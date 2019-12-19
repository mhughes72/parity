from django.contrib import admin

# Import all House related classes
from .models import House, Room, Thermostat, Light, SensorTemperatureIndoor

# Specify what fields will show up in the Admin
class HouseAdmin(admin.ModelAdmin):
    fields = ['label', 'room', 'thermostat']

class RoomAdmin(admin.ModelAdmin):
    fields = ['label', 'light', 'sensor_temperature_indoor']

class ThermostatAdmin(admin.ModelAdmin):
    fields = ['label', 'thermostat_mode']

class LightAdmin(admin.ModelAdmin):
    fields = ['label', 'light_on']

class SensorTemperatureIndoorAdmin(admin.ModelAdmin):
    fields = ['label', 'temperature']


# Register the above with the admin.site
admin.site.register(House, HouseAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Thermostat, ThermostatAdmin)
admin.site.register(Light, LightAdmin)
admin.site.register(SensorTemperatureIndoor, SensorTemperatureIndoorAdmin)



