from django.urls import path

from .views import *


app_name = 'agendamento_laboratorio'
urlpatterns = [
    path('criar/', AgendamentoLaboratorioCreateView.as_view(), name='criar_agendamento'),
    path('', AgendamentoLaboratorioListView.as_view(), name='list_agendamento'),
]
