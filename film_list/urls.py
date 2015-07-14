from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'film_list.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^first_view/(?P<starts_with>\w+)$', 'main.views.first_view'),
    url(r'^first_view/$', 'main.views.first_view'),
    url(r'^get_post/$', 'main.views.get_post'),
)
