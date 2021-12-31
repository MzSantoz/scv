import uuid
from django.db import models

class Indicacao(models.TextChoices):
    SIM = 'S', 'Sim'
    NAO = 'N', 'Não'

def diretorio_empresa(instance, filename):
  return 'empresa_{0}/{1}'.format(instance.empresa.id, filename)


class Empresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    razao_social = models.CharField(max_length=255, verbose_name="Razão Social")
    indicado = models.CharField(max_length=1, choices=Indicacao.choices, default=Indicacao.NAO, verbose_name="Indicação ?")
    data_da_visita = models.DateField(verbose_name="Data da Visita")
    atividade = models.TextField(max_length=200, null=True, blank=True, verbose_name="Atividade")
    endereco = models.TextField(max_length=255, null=True, blank=True, verbose_name="Endereço")
    briefing = models.TextField(max_length=255, null=True, blank=True, verbose_name="Briefing")

    class Meta:
        verbose_name = "Empresa"
    
    def __str__(self):
        return self.razao_social


class Documento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=200, verbose_name="Nome do Documento")
    arquivo = models.FileField(upload_to=diretorio_empresa, null=True, blank=True, verbose_name="Arquivo")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Empresa")

    def __str__(self):
        return self.nome