from django.shortcuts import render
from django.http import HttpResponse

from main.models import Film
# Create your views here.


def first_view(request):
    text_string = ''

    films = Film.objects.filter(title__startswith='Z')

    for film in films:
        text_string += 'Title: %s | Year: %s </br>' % (film.title, film.year)

    return HttpResponse(text_string)
