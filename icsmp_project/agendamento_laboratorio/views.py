from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import AgendamentoLaboratorio


class AgendamentoLaboratorioCreateView(CreateView):
    template_name = "agendamento_laboratorio/create.html"
    model = AgendamentoLaboratorio
    fields = '__all__'
    success_url = reverse_lazy('agendamento_laboratorio:list_agendamento')


class AgendamentoLaboratorioListView(ListView):
    template_name = "agendamento_laboratorio/list.html"
    model = AgendamentoLaboratorio
    context_object_name = "agendamentos"
