from django.urls import path

from icsmp_project.modulos_aulas.views import detalhe, aula

app_name = 'modulos_aulas'
urlpatterns = [
    path('<slug:slug>', detalhe, name='detalhe'),
    path('aulas/<slug:slug>', aula, name='aula'),
]
