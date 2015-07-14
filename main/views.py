from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape

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


def get_post(request):
    get_title = request.GET.get('title', None)
    print get_title
    title_string = ''
    films = Film.objects.filter(title__contains='%s' % get_title)
    for film in films:
        title_string += '%s <br>' % film.title

    title_string += """
    <form action="/get_post" method="GET"

    Title:
    <br>
    <input type="text" name="title">

    <br>
    <br>
    <input type="submit" value="submit"

    </form>
    """

    response = title_string
    return HttpResponse(response)
