from .base import BaseModel
from django.db import models

class Questionario(BaseModel):

    nome_paciente = models.CharField(max_length=255)
    numero_telefone = models.CharField(max_length=20)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)



    

    def __str__(self):
        return self.nome