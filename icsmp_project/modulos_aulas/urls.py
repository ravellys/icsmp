from django.urls import path

from icsmp_project.modulos_aulas.views import detalhe

app_name = 'modulos_aulas'
urlpatterns = [
    path('<slug:slug>', detalhe, name='detalhe'),
]
