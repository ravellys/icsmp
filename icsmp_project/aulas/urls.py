from django.urls import path

from icsmp_project.aulas.views import video, indice, palavra_count

app_name = 'aulas'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('palavra_count/', palavra_count, name='palavra_count'),
    path('', indice, name='indice'),
]
