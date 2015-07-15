from django.db import models

# Create your models here.

# Year;Length;Title ;Subject;Actor;Actress;Director;Popularity;Awards;*Image


class Film(models.Model):
    year = models.ForeignKey('main.Year', null=True)
    length = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True, unique=True)
    genre = models.ForeignKey('main.Genre', null=True)
    popularity = models.IntegerField(null=True, blank=True)
    awards = models.CharField(max_length=100, null=True, blank=True)
    director = models.ForeignKey('main.Director', null=True)
    actor = models.ForeignKey('main.Actor', null=True)
    actress = models.ForeignKey('main.Actress', null=True)

    def __unicode__(self):
        return self.title


class Year(models.Model):
    year = models.IntegerField(null=True, blank=True, unique=True)

    def __unicode__(self):
        return self.year


class Genre(models.Model):
    genre = models.CharField(max_length=100, null=True, blank=True, unique=True)

    def __unicode__(self):
        return self.genre


class Director(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, unique=True)

    verbose_name = 'Director'
    verbose_name_plural = 'Directors'

    def __unicode__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, unique=True)

    verbose_name = 'Actor'
    verbose_name_plural = 'Actors'

    def __unicode__(self):
        return self.name


class Actress(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, unique=True)

    verbose_name = 'Actress'
    verbose_name_plural = 'Actresses'

    def __unicode__(self):
        return self.name
