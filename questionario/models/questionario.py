from .base import BaseModel
from django.db import models
from conta.models.paciente import Paciente

class Questionario(BaseModel):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return self.paciente.nome