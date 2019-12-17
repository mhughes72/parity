from django.db import models

class Light(models.Model):
    label = models.CharField(max_length=255, blank=True)
    light_on = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        print("LIGHT UPDATE")
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.label

class SensorTemperatureIndoor(models.Model):
    label = models.CharField(max_length=255, blank=True)
    temperature = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        print("SENSOR UPDATE")
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.label

class Room(models.Model):
    label = models.CharField(max_length=255, blank=True)
    light = models.ManyToManyField(Light, blank=True)
    sensor_temperature_indoor = models.ManyToManyField(SensorTemperatureIndoor, blank=True)

    def save(self, *args, **kwargs):
        print("ROOM UPDATE")
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.label

class Thermostat(models.Model):

    THERMOSTAT_MODES = (
        ('OFF', 'Off'),
        ('COOL', 'Cool'),
        ('HEAT', 'Heat'),
        ('FAN_OFF', 'Fan-on'),
        ('AUTO', 'Auto'),
    )
    label = models.CharField(max_length=255, blank=True)
    thermostat_mode = models.CharField(max_length=10, choices=THERMOSTAT_MODES)

    def save(self, *args, **kwargs):
        print("THERMOSTAT UPDATE")
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.label

class House(models.Model):
    label = models.CharField(max_length=255, blank=True)
    room = models.ManyToManyField(Room, blank=True)
    thermostat = models.ManyToManyField(Thermostat, blank=True)

    def save(self, *args, **kwargs):
        print("HOUSE UPDATE")
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.label









#********************************************

class SensorHumidityIndoor(models.Model):
    #Placeholder for future expansion
    pass

class SensorTemperatureOutdoor(models.Model):
    # Placeholder for future expansion
    pass
