from .base import BaseModel
from django.db import models
from conta.models.paciente import Paciente
from conta.models.usuario import Usuario
class Questionario(BaseModel):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    avaliador = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    data = models.DateField()
    respostas = models.JSONField()
    def __str__(self):
        return self.paciente.nome