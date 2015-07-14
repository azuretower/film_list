from django.contrib import admin
from main.models import Film, Director, Actor, Actress
# Register your models here.


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'popularity', 'year')
    search_fields = ['title', 'genre', 'popularity', 'year']


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


class ActorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


class ActressAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


admin.site.register(Film, FilmAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Actress, ActressAdmin)
