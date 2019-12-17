from django.contrib import admin

from .models import House, Room, Thermostat, Light, SensorTemperatureIndoor


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


admin.site.register(House, HouseAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Thermostat, ThermostatAdmin)
admin.site.register(Light, LightAdmin)
admin.site.register(SensorTemperatureIndoor, SensorTemperatureIndoorAdmin)



