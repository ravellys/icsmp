from django.db import models

# Create your models here.
from django.urls import reverse
from ordered_model.models import OrderedModel


class ModuloArtigo(OrderedModel):
    nome = models.CharField(max_length=32)
    descricao = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('modulos_artigos:modulo_detalhe', kwargs={'slug': self.slug})


class Artigo(OrderedModel):
    modulo = models.ForeignKey(ModuloArtigo, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=32)
    autor = models.TextField(null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(unique=True)
    order_with_respect_to = 'modulo'

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos_artigos:artigo_detalhe', kwargs={'slug': self.slug})
