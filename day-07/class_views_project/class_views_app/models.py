from django.db import models

class Weather(models.Model):
    date = models.DateTimeField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    temp_f = models.FloatField()
    condition = models.CharField(max_length=100)
    wind_speed_mph = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.temp_f}"
