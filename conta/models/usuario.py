from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from base import BaseModel
data = datetime.now()

class Usuario(BaseModel):
    """A classe Corredor é responsável pelo cadastro de usuários na aplicação WEB"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    email = models.EmailField()

    numero_telefone = models.CharField(max_length=11)
    data_nascimento = models.DateField(default=timezone.now())
    senha = models.CharField(max_length=100)
    nome_de_usuario = models.CharField(max_length=100, validators=[MinLengthValidator(3), MaxLengthValidator(100)])
    class Meta:
        """Documentação da classe Meta"""
        pass
    
    def __str__(self):
        """ metodo para retornar o objeto """
        return self.nome
    