from django.forms import ModelForm
from conta.models.usuario import Usuario
from django.contrib.auth.models import User
from conta.models.paciente import Paciente

class UserForm(ModelForm):
    """ formulario para criar um usuário """
    class Meta:
        """ classe meta """
        model = User
        fields = ['username', 'password']

class UsuarioForm(ModelForm):
    """ formulario para criar um usuario """
    class Meta:
        """ classe meta """
        model = Usuario
        fields = ['nome', 'email', 'numero_telefone', 'data_nascimento']


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente

        fields = ['nome', 'email', 'cpf', 'numero_telefone', 'idade']
    