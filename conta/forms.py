from django.forms import ModelForm
from django import forms
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

        fields = ['nome', 'email', 'cpf', 'numero_telefone', 'idade', 'sexo', 'raca', 'estatura', 'peso']

class QuestionarioSarcopeniaForm(forms.Form):


    OPCOES_FORCA = [
        ('0', '0 - Nenhuma dificuldade'), 
        ('1', '1 - Alguma dificuldade'),
        ('2', '2 - Muita dificuldade/não consegue'),]
    
    forca = forms.ChoiceField(
        label="Quanta dificuldade você tem para levantar e carregar 5 kg?",
        choices=OPCOES_FORCA,
        widget=forms.RadioSelect,
        required=True
    )

    OPCOES_CAMINHADA = [
        ('0', '0 - Nenhuma dificuldade'), 
        ('1', '1 - Alguma dificuldade'),
        ('2', '2 - Muita/Usa apoios/Incapaz'),]
    ajuda_caminhada = forms.ChoiceField(
        label="Quanta dificuldade você tem para atravessar um cômodo?",
        choices=OPCOES_CAMINHADA,
        widget=forms.RadioSelect,
        required=True
    )

    OPCOES_LEVANTAR = [
        ('0', '0 - Nenhuma dificuldade'), 
        ('1', '1 - Alguma dificuldade'),
        ('2', '2 - Muita/Não consegue sem ajuda'),]
    
    levantar = forms.ChoiceField(
        label="Quanta dificuldade você tem para levantar-se de uma cama ou cadeira?",
        choices=OPCOES_LEVANTAR,
        widget=forms.RadioSelect,
        required=True,)
    
    OPCOES_SUBIR = [
        ('0', '0 - Nenhuma dificuldade'), 
        ('1', '1 - Alguma dificuldade'),
        ('2', '2 - Muita dificuldade/não consegue'),]
    subir = forms.ChoiceField(
        label="Quanta dificuldade você tem para subir um lance de escadas de 10 degraus?",
        choices=OPCOES_SUBIR,
        widget=forms.RadioSelect,
        required=True,)
    
    OPCOES_QUEDA = [
        ('0', '0 - Nenhuma'), 
        ('1', '1 - (1 A 3) Quedas'),
        ('2', '2 - (4 ou Mais) Quedas'),]
    
    queda = forms.ChoiceField(
        label="Quantas vezes você caiu nos últimos 12 meses?",
        choices=OPCOES_QUEDA,
        widget=forms.RadioSelect,
        required=True,)
    
    circunferencia_panturrilha = forms.IntegerField(
        label="Medir circunferência da perna direita com paciente em pé, com os pés afastados 20cm e com as pernas relaxadas.",
        required=True
    )


class QuestionarioSegundaEtapaForm(forms.Form):

    OPCOES_SEGUNDA_ETAPA = [
        ('Levantar/Sentar', 'Levantar/Sentar de uma cadeira sem usar os braços 5 vezes'),
        ('Forca Preensar', 'Forca Preensar com dinamômetro')
    ]

    segunda_etapa = forms.ChoiceField(
        label="Selecione a avaliação da segunda etapa:",
        choices=OPCOES_SEGUNDA_ETAPA,
        widget=forms.RadioSelect,
        required=True
    )

    valor_segunda_etapa = forms.IntegerField(
        label="Insira o valor obtido na avaliação selecionada:",
        required=True
    )

class QuestionarioTerceiraEtapaForm(forms.Form):

    OPCOES_TERCEIRA_ETAPA = [
        ('MMEA', 'Peso da massa esqueletica dos membros inferiores (MMEA)'),
        ('Equacao de Lee', 'Calcula o IMMEA usando a equação de Lee et al.'),
    ]

    terceira_etapa = forms.ChoiceField(
        label="Selecione a avaliação da terceira etapa:",
        choices=OPCOES_TERCEIRA_ETAPA,
        widget=forms.RadioSelect,
        required=True
    )

    valor_terceira_etapa = forms.IntegerField(
        label="Insira o valor obtido na avaliação selecionada:",
        required=False
    )

class QuestionarioQuartaEtapaForm(forms.Form):

    valor_quarta_etapa = forms.IntegerField(
        label="Insira o tempo (em segundos) para completar o teste de caminhada de 4 metros:",
        required=True
    )