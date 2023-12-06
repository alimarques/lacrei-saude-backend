import datetime

from django.db import models


class Profissional(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    nome_social = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_social

class Consulta(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_consulta = models.DateTimeField(default=datetime.datetime.now)
    profissional = models.ForeignKey(
        Profissional, on_delete=models.SET_NULL, null=True
    )
