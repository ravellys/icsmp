from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Img3d(OrderedModel):
    nome = models.CharField(max_length=32, unique=True)
    descricao = models.TextField(null=True, blank=True)
    trabalhos_utilizados = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    arquivo = models.FileField()
    url = models.CharField(max_length=200, null=True, blank=True)

    class Meta(OrderedModel.Meta):
        pass

    def save(self, *args, **kwargs):
        self.url = self.arquivo.url
        super(Img3d, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('modulos_artigos:modulo_detalhe', kwargs={'slug': self.slug})
