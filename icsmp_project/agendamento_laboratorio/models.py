from django.db import models


class NivelCurso(models.Model):
    """
    Nivel do curso mestradado/doutorado/graduação
    """
    ativo = models.BooleanField(default=False, null=False)
    nome = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nome

class AgendamentoLaboratorio(models.Model):
    nome = models.CharField(max_length=100, null=False)
    nivel_curso = models.ForeignKey(NivelCurso, on_delete=models.DO_NOTHING, null=False)
    # cpf = models.CharField(max_length=11, null=True)
    # rg = models.CharField(max_length=11, null=True)
    # endereco = models.TextField()
    telefone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=100, null=False)

    projeto = models.TextField(default=None, null=True, blank=True)
    orientador = models.CharField(max_length=100, null=True)
    email_orientador = models.CharField(max_length=100, null=True)

    programa = models.CharField(max_length=100, null=True)
    descricao_amostras = models.TextField(default=None, null=True, blank=True)
    quantidade_amostras = models.IntegerField(null=True)
    numero_escaneamentos = models.IntegerField(null=True)
    observacao = models.TextField(default=None, null=True, blank=True)

    data_gravacao = models.DateTimeField(null=False, auto_now_add=True)
    data_alteracao = models.DateTimeField(null=True, auto_now=True)
    data_solicitacao = models.DateTimeField(null=False)
    ativo = models.BooleanField(default=True, null=False)

