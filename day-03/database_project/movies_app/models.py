from django.db import models

# MVC - model view controller

# MODEL --> is a way to interface with the database --> talk to the db

class Movie(models.Model):
    # each movie also gets an id
    title = models.CharField() # charfield is for strings
    release_year = models.IntegerField(default=2026)
    run_time = models.IntegerField()
    genre = models.CharField()
    description = models.TextField() # longer strings
    rating = models.IntegerField( null=True )
    
    # shows the movie as just a string (in this case show the title of the movie)
    def __str__(self):
        return f"{self.title} - {self.genre}"


# INHERITANCE #

# class Cat:
#     def meow(self):
#         print("MEOW")
        
# class Lion(Cat):        

#     def roar(self):
#         print("RAAAAWWWWR")