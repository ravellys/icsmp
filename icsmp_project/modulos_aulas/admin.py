from django.contrib import admin

# Register your models here.
from ordered_model.admin import OrderedModelAdmin

from icsmp_project.modulos_aulas.models import ModuloAula, Aula


@admin.register(ModuloAula)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('nome', 'descricao', 'move_up_down_links')
    prepopulated_fields = {'slug': ('nome', )}

@admin.register(Aula)
class AulaAdmin(OrderedModelAdmin):
    list_display = ('nome', 'descricao', 'move_up_down_links')
    ordering = ('modulo', 'order')
    prepopulated_fields = {'slug': ('nome', )}
