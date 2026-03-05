from django.db import models


class Anime(models.Model):

    # attributes / db columns
    # by default we always get an id
    name = models.CharField(max_length=300)
    main_character = models.CharField(max_length=300)
    num_seasons = models.IntegerField()

    def __str__(self):
        return self.name

    # CREATE
    # naruto = Anime(name="Naruto", main_character="Naruto", num_seasons=5)
    # naruto.save()

    # SAVE
    # naruto.num_seasons = 6
    # naruto.save()

    # DELETE
    # naruto.delete()