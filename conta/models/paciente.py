from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from .base import BaseModel
from .usuario import Usuario

class Paciente(BaseModel):
    """A classe Paciente é responsável pelo cadastro de pacientes na aplicação WEB"""
    nome = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    email = models.EmailField()
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)], unique=True)
    numero_telefone = models.CharField(max_length=11)
    idade = models.IntegerField(null=True, blank=True)


    avaliador = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    


    class Meta:
        """Documentação da classe Meta"""
        pass
    
    def __str__(self):
        """ metodo para retornar o objeto """
        return self.nome