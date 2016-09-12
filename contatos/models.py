from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=80)
    idade = models.PositiveIntegerField()
    site = models.URLField()
    datacadastro = models.DateField()

    def __str__(self):
        return "%s - %s" % (self.nome, self.site)