from django.contrib.admin import ModelAdmin, register

from icsmp_project.aulas.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('titulo', 'slug', 'creation', 'v_id')
    ordering = ('creation', 'titulo')
    prepopulated_fields = {'slug': ('titulo',)}
