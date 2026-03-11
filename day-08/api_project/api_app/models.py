from django.db import models


class MarsRoverPart(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    purpose = models.TextField()
    serial_number = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
    



class Rover(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name