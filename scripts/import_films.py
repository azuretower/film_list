#!/usr/bin/env python
import csv
import os
import sys
import unicodedata
import codecs
from unidecode import unidecode


sys.path.append("..")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'film_list.settings')

from main.models import Film, Director, Actor, Actress
csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'film.csv')
csv_file = open(csv_path, 'rU')
reader = csv.DictReader(csv_file, delimiter=';')

for row in reader:
    try:
        director = unidecode(row['director'])
        new_director, created = Director.objects.get_or_create(name=director)
    except TypeError, e:
        print e
        director = row['director']
        new_director, created = Director.objects.get_or_create(name=director)
    new_director.save()

    try:
        actor = unidecode(row['actor'])
        new_actor, created = Actor.objects.get_or_create(name=actor)
    except TypeError, e:
        print e
        actor = row['actor']
        new_actor, created = Actor.objects.get_or_create(name=actor)
    new_actor.save()

    try:
        actress = unidecode(row['actress'])
        new_actress, created = Actress.objects.get_or_create(name=actress)
    except TypeError, e:
        print e
        actress = row['actress']
        new_actress, created = Actress.objects.get_or_create(name=actress)
    new_actress.save()

    new_film, created = Film.objects.get_or_create(title=row['title'])
    new_film.year = int(row['year'])
    try:
        new_film.length = int(row['length'])
    except ValueError, e:
        pass
    new_film.genre = row['genre']
    try:
        new_film.popularity = int(row['popularity'])
    except ValueError, e:
        pass
    new_film.awards = row['awards']
    new_film.director = new_director
    new_film.actor = new_actor
    new_film.actress = new_actress
    new_film.save()

csv_file.close()
