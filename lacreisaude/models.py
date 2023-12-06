from django.db import models


class Profissional(models.Model):
    nome_social = models.CharField(max_length=100)

class Consulta(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    profissional = models.ForeignKey(
        Profissional, on_delete=models.SET_NULL, null=True
    )
