from django.contrib import admin

# Register your models here.
from ordered_model.admin import OrderedModelAdmin
from icsmp_project.img3d.models import Img3d


@admin.register(Img3d)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('nome', 'descricao', 'move_up_down_links')
    prepopulated_fields = {'slug': ('nome', )}
