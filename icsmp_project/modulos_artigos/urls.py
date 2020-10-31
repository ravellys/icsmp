from django.urls import path

from icsmp_project.modulos_artigos.views import ModulosArtigosListView, ModuloUpdateView, ArtigoUpdateView


app_name = 'modulos_artigos'
urlpatterns = [
    path('', ModulosArtigosListView.as_view(), name='lista_modulos'),
    path('<slug:slug>', ModuloUpdateView.as_view(), name='modulo_detalhe'),
    path('artigos/<slug:slug>', ArtigoUpdateView.as_view(), name='artigo_detalhe'),
]
