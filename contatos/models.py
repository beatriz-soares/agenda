from __future__ import unicode_literals

from django.db import models

# Create your models here.

MASCULINO = 'M'
FEMININO = 'F'

SEXO_CHOICES = (
    (MASCULINO, 'Masculino'),
    (FEMININO, 'Ferminino'),
)

RESIDENCIAL = 'Residencial'
MOVEL = 'Movel'

TIPO_NUM = (
    (RESIDENCIAL, 'Residencial'),
    (MOVEL, 'Movel'),
)


class Pessoa(models.Model):
    nome = models.CharField(max_length=80)
    idade = models.PositiveIntegerField()
    site = models.URLField()
    datacadastro = models.DateField()
    sexo = models.CharField(
        max_length=2,
        choices=SEXO_CHOICES,
        default=FEMININO,
    )

    def __str__(self):
        return "%s - %s" % (self.nome, self.site)


class Numero(models.Model):
    pessoa = models.ForeignKey(Pessoa, related_name="numeros")
    numero = models.CharField(max_length=11)
    tiponum = models.CharField(
        max_length=20,
        choices=TIPO_NUM,
        default=MOVEL,
    )