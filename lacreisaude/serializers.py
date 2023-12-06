from rest_framework import serializers

from .models import Consulta, Profissional


class ProfissionalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profissional
    fields = [
      'id',
      'nome_social',
      'data_criacao',
    ]

class ConsultaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Consulta
    fields = [
      'id',
      'data_criacao',
      'data_consulta',
      'profissional',
    ]