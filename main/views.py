from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from main.models import Film, Director, Actor, Actress, Year, Genre
# Create your views here.


def template_view(request):
    context = {}
    years = Year.objects.all()
    context['years'] = years
    return render(request, 'base.html', context)


def first_view(request, starts_with):
    text_string = ''

    films = Film.objects.all()

    years = Year.objects.filter(year__contains='%s' % starts_with)

    for year in years:
        films = year.film_set.all()

        for film in films:
            text_string += 'Title: %s  | Year: %s </br>' % (film.title, str(year.year))

    return HttpResponse(text_string)


@csrf_exempt
def get_post(request):
    get_title = request.POST.get('title', None)
    print get_title
    title_string = ''

    title_string += """
    <form action="/get_post/" method="POST"

    Title:
    <br>
    <input type="text" name="title">

    <br>
    <br>
    <input type="submit" value="submit"

    </form>
    <br>
    <br>
    """

    films = Film.objects.filter(title__contains='%s' % get_title)
    for film in films:
        title_string += '%s <br>' % film.title

    response = title_string
    return HttpResponse(response)


class GetPost(View):
    form = """
        <form action="/GetPost/" method="POST">

            Title:
            <br>
            <input type="text" name="title">
            <br>

            <br>
            <input type="submit" value="submit"

            <br>
            <br>
            </form>
        """

    def get(self, request, *args, **kwargs):

        return HttpResponse(self.form)

    def post(self, request, *args, **kwargs):
        get_title = request.POST.get('title', None)
        print get_title
        title_string = ''
        films = Film.objects.filter(title__contains='%s' % get_title)
        for film in films:
            self.form += '%s <br>' % film.title

        response = self.form
        return HttpResponse(response)
