from django.shortcuts import render
from django.http import HttpResponse

from main.models import Film, Director, Actor, Actress
# Create your views here.


def first_view(request, starts_with):
    text_string = ''

    films = Film.objects.all()

    directors = Director.objects.filter(name__contains='%s' % starts_with)

    for director in directors:
        films = director.film_set.all()

        for film in films:
            text_string += 'Title: %s  | Director: %s </br>' % (film.title, director.name)

    return HttpResponse(text_string)
