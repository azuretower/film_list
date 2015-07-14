from django.db import models

# Create your models here.

# Year;Length;Title ;Subject;Actor;Actress;Director;Popularity;Awards;*Image
# INT ;INT   ;STRING;CAT    ;CAT  ;CAT    ;CAT     ;INT       ;BOOL  ;STRING


class Film(models.Model):
    year = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True, unique=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    popularity = models.IntegerField(null=True, blank=True)
    awards = models.CharField(max_length=100, null=True, blank=True)
    director = models.ForeignKey('main.Director', null=True)
    actor = models.ForeignKey('main.Actor', null=True)
    actress = models.ForeignKey('main.Actress', null=True)

    def __unicode__(self):
        return self.title


class Director(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, unique=True)

    verbose_name = 'Director'
    verbose_name_plural = 'Directors'

    def __unicode__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, unique=True)

    verbose_name = 'Actor'
    verbose_name_plural = 'Actors'

    def __unicode__(self):
        return self.title


class Actress(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, unique=True)

    verbose_name = 'Actress'
    verbose_name_plural = 'Actresses'

    def __unicode__(self):
        return self.title
