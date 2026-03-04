from django.db import models
from datetime import datetime

# any time I make a change inside of models.py
# python manage.py makemigrations
# python manage.py migrate

# MVC - model view controller

# MODEL --> is a way to interface with the database --> talk to the db


class Genre(models.Model):
    name = models.CharField()
    
    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    # each movie also gets an id
    title = models.CharField() # short strings
    release_year = models.IntegerField( default=2026 )
    run_time = models.IntegerField()
    description = models.TextField() # longer strings
    rating = models.IntegerField( null=True, blank=True )
    
    # max_digits means we can't go higher than 999.99
    # decimal_places means there will always be two decimals (0.01)
    rental_price = models.DecimalField( max_digits=5, decimal_places=2, default=1.95 )
    
    genres = models.ManyToManyField(Genre, blank=True)
    
    # auto_now_add triggers whenever something gets created
    created_at = models.DateTimeField( auto_now_add=True )
    # auto_now triggers whenever something gets updated
    updated_at = models.DateTimeField( auto_now=True )
    
    # shows the movie as just a string (in this case show the title of the movie)
    def __str__(self):
        return f"{self.title}"


class MovieCharacter(models.Model):
    name = models.CharField()
    special_power = models.CharField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="characters")
                    # 1. the model we're associating with
                    # 2. what happens when we delete a movie (delete all movie characters)
                    #  3. what we can call on a movie to see all its characters
    def __str__(self):
        return f"{self.name} - {self.movie}"


# INHERITANCE #

# class Cat:
#     def meow(self):
#         print("MEOW")
        
# class Lion(Cat):        

#     def roar(self):
#         print("RAAAAWWWWR")