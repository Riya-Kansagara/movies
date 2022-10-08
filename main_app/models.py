from enum import unique
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Genre(models.Model):
    genre_title = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.genre_title

class Movie(models.Model):
    title = models.CharField(_("movie title"), max_length=250, unique=True) 
    year = models.BigIntegerField(_("released year"))
    rating = models.IntegerField(_("rating"), default=0)
    genres = models.ManyToManyField(Genre, verbose_name=_("Genre"))

    def __str__(self):
        return self.title
    
