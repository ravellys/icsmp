from django.db import models

# Create your models here.
from django.urls import reverse
from ordered_model.models import OrderedModel


class ModuloAula(OrderedModel):
    nome = models.CharField(max_length=32)
    descricao = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('modulos_aulas:detalhe', kwargs={'slug': self.slug})


class Aula(OrderedModel):
    nome = models.CharField(max_length=32)
    descricao = models.TextField()
    slug = models.SlugField(unique=True)
    modulo = models.ForeignKey(ModuloAula, on_delete=models.PROTECT)
    order_with_respect_to = 'modulo'
    v_id = models.CharField(max_length=32)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('modulos_aulas:aula', kwargs={'slug': self.slug})
