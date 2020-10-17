from django.urls import path

from icsmp_project.aulas.views import video

app_name = 'aulas'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
]
