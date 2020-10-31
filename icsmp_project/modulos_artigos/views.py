from django.views.generic import ListView, UpdateView
from icsmp_project.modulos_artigos.models import ModuloArtigo, Artigo


class ModulosArtigosListView(ListView):
    template_name = "modulos_artigos/lista_modulos_artigos.html"
    model = ModuloArtigo
    context_object_name = "modulos_artigos"


class ModuloUpdateView(UpdateView):
    template_name = "modulos_artigos/modulo_detalhe.html"
    model = ModuloArtigo
    fields = '__all__'
    context_object_name = 'modulo'


class ArtigosListView(ListView):
    template_name = "modulos_artigos/modulo_detalhe.html"
    model = ModuloArtigo
    context_object_name = "modulos_artigos"


class ArtigoUpdateView(UpdateView):
    template_name = "modulos_artigos/artigo_detalhe.html"
    model = Artigo
    fields = '__all__'
    context_object_name = 'artigo'
