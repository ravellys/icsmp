from django.contrib import admin

# Register your models here.
from ordered_model.admin import OrderedModelAdmin

from icsmp_project.modulos_artigos.models import ModuloArtigo, Artigo


@admin.register(ModuloArtigo)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('nome', 'descricao', 'move_up_down_links')
    prepopulated_fields = {'slug': ('nome', )}


@admin.register(Artigo)
class ArtigoAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'modulo', 'move_up_down_links')
    ordering = ('modulo', 'order')
    prepopulated_fields = {'slug': ('titulo', )}
