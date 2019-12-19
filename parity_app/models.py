#MODELS for House
#5 active classes and 2 placeholders for future development
# @House has a foreign key relationship with @Thermostat and @Room
# @Room has a foreign key relationship with @Light and @SensorTemperatureIndoor

from django.db import models

# Light class represents indoor lights that can appear in a Room
class Light(models.Model):

    # label is for identification purposes.
    label = models.CharField(max_length=255, blank=True)

    # A light can only have 2 states, on or NOT on.
    light_on = models.BooleanField(default=False)

    # Save method is called when any change is made to the Model's values.
    def save(self, *args, **kwargs):
        print("LIGHT UPDATE")
        # When requirements are defined we will override the save method with appropriate actions.
        super().save(*args, **kwargs)

    def __str__(self):
        return self.label


# SensorTemperatureIndoor class represents indoor temperature sensors that can appear in a Room
class SensorTemperatureIndoor(models.Model):

    # label is for identification purposes.
    label = models.CharField(max_length=255, blank=True)

    # Temperature is currently an unbounded Integer, we will probably want to limit the value possibilities
    # Also an empty field is currently not allowed.  Will have to follow up on requirements
    temperature = models.IntegerField(null=True, default=17)

    # Save method is called when any change is made to the Model's values.
    def save(self, *args, **kwargs):
        print("SENSOR UPDATE")
        # When requirements are defined we will override the save method with appropriate actions.
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.label


# Room class represents rooms that can appear in a House
class Room(models.Model):

    # label is for identification purposes.
    label = models.CharField(max_length=255, blank=True)

    # An instance of a light object
    light = models.ManyToManyField(Light, blank=True)

    # An instance of an Indoor Temperature Sensor
    sensor_temperature_indoor = models.ManyToManyField(SensorTemperatureIndoor, blank=True)

    # Save method is called when any change is made to the Model's values.
    def save(self, *args, **kwargs):
        print("ROOM UPDATE")
        # When requirements are defined we will override the save method with appropriate actions.
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.label


# Thermostat class represents thermostats that can appear in a House
# Currently a House can contain many thermostats.  Not sure if this should have an upper limit?  (ie 1?)
class Thermostat(models.Model):

    # Define the possible values that a thermostat can have
    THERMOSTAT_MODES = (
        ('OFF', 'Off'),
        ('COOL', 'Cool'),
        ('HEAT', 'Heat'),
        ('FAN_OFF', 'Fan-on'),
        ('AUTO', 'Auto'),
    )

    # label is for identification purposes.
    label = models.CharField(max_length=255, blank=True)

    # instance of a thermostat
    thermostat_mode = models.CharField(max_length=10, choices=THERMOSTAT_MODES, default='OFF')

    # Save method is called when any change is made to the Model's values.
    def save(self, *args, **kwargs):

        print("THERMOSTAT UPDATE")
        # When requirements are defined we will override the save method with appropriate actions.
        super().save(*args, **kwargs)

    def __str__(self):
        return self.label


# House is the toppermost Model which can contain thermostats and rooms.
class House(models.Model):

    # label is for identification purposes.
    label = models.CharField(max_length=255, blank=True)

    # instance of a room
    room = models.ManyToManyField(Room, blank=True)

    # instance of a thermostat
    thermostat = models.ManyToManyField(Thermostat, blank=True)

    # Save method is called when any change is made to the Model's values.
    def save(self, *args, **kwargs):
        print("HOUSE UPDATE")
        # When requirements are defined we will override the save method with appropriate actions.
        super().save(*args, **kwargs)

    def __str__(self):
        return self.label


#********************************************
# Holding classes for future use
class SensorHumidityIndoor(models.Model):
    #Placeholder for future expansion
    pass

class SensorTemperatureOutdoor(models.Model):
    # Placeholder for future expansion
    pass
