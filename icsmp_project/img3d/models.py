from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Img3d(OrderedModel):
    nome = models.CharField(max_length=32)
    descricao = models.TextField(null=True, blank=True)
    trabalhos_utilizados = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    arquivo = models.FileField()

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('modulos_artigos:modulo_detalhe', kwargs={'slug': self.slug})
