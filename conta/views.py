from django.shortcuts import render, get_object_or_404, redirect
from conta.models.usuario import *
from conta.models.paciente import Paciente
from questionario.models.questionario import Questionario
from .forms import UserForm, UsuarioForm, PacienteForm, QuestionarioSarcopeniaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django import template
from django.template.defaultfilters import stringfilter
import time

register = template.Library()

@register.filter(name='split')
@stringfilter
def split(string, sep):
    """Return the string split by sep.

    Example usage: {{ value|split:"/" }}
    """
    return string.split(sep)


def create_user(request):
    """ Esta view é responsável por criar um User e um Corredor """
    mensagem = ''
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_usuario = UsuarioForm(request.POST)

        if form_user.is_valid() and form_usuario.is_valid():

            user = form_user.save()
            user.password =make_password(form_user.cleaned_data['password'])
            checkpassword=check_password(request.POST['password'], user.password)
            user_id = user.id
            print(user.password)
            user.save()
            print(user.password)
            form_instante = Usuario()
            form_instante.id = user_id
            form_instante.user = user

            form_instante.nome = form_usuario.cleaned_data['nome']
            form_instante.email = form_usuario.cleaned_data['email']
            form_instante.numero_telefone = form_usuario.cleaned_data['numero_telefone']
            form_instante.data_nascimento = form_usuario.cleaned_data['data_nascimento']

            form_instante.senha = form_user.cleaned_data['password']
            form_instante.nome_de_usuario = form_user.cleaned_data['username']

            form_instante.save()

            mensagem = 'Usuário criado com sucesso'
            return redirect('login')
    else:
        form_user = UserForm()
        form_usuario = UsuarioForm()

    context = {
        'mensagem': mensagem,
        'form_user': form_user,
        'form_usuario': form_usuario,
    }
    return render(request, 'conta/create_user.html', context)

@login_required
def usuario_delete(request, usuario_id):
    """ Esta view é responsável por deletar o Usuario e User do usuário logado """
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    user = usuario.user
    mensagem = ''
    time.sleep(3)
    try:
        usuario.delete()
        user.delete()
        mensagem = 'Usuario apagado com sucesso'
        return redirect('login')
    except:
        context = {
            'mensagem': mensagem
        }
    return render(request, 'content.html', context)

@login_required
def usuario_update(request, user_id):
    """ Esta view é responsável por atualizar o perfil do usuario """
    usuario = get_object_or_404(Usuario, pk=user_id)
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST, instance=usuario)
        if usuario_form.is_valid():
            usuario_form.save()

            return redirect('index')

    else:
        usuario_form = UsuarioForm(instance=usuario)
    context = {
        'usuario_form': usuario_form,
        'usuario': usuario,
        'footer_position' : 'absolute',
    }
    return render(request, 'conta/usuario_update.html', context)

@login_required
def usuario_list(request, usuario_id):
    """ Esta view é responsável por listar todos os usuario que estão cadastrados no banco de dados """
    avaliador = get_object_or_404(Usuario, pk=usuario_id)
    usuarios = Paciente.objects.all()
    usuarios_validados = []
    for paciente in usuarios:
        if paciente.avaliador == avaliador:
            usuarios_validados.append(paciente)
    context = {
        'pacientes': usuarios_validados
    }

    return render(request, 'conta/usuario_list.html', context)

@login_required
def usuario_read(request, usuario_id):
    """ Esta view é responsável por exibir os detalhes de um usuario específico """
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    context = {
        'usuario': usuario,
        'footer_position' : 'absolute',
    }
    return render(request, 'conta/usuario_read.html', context)

def sobre(request):
    """ Esta view é responsável por exibir a página sobre """
    return render(request, 'conta/sobre.html')

@login_required
def paciente_create(request, usuario_id):
    """ Esta view é responsável por exibir os detalhes de um usuario específico """
    usuario = get_object_or_404(Usuario, pk=usuario_id)

    if request.method == 'POST':
        paciente_form = PacienteForm(request.POST)
        if paciente_form.is_valid():
            paciente = paciente_form.save()
            paciente.avaliador = usuario
            paciente.save()

            return redirect('usuario_list', usuario_id=usuario.id)
    else:
        paciente_form = PacienteForm()
    context = {
        'usuario': usuario,
        'form_paciente': paciente_form,
    }

    return render(request, 'conta/paciente_create.html', context)

@login_required
def paciente_update(request, paciente_cpf):
    """ Esta view é responsável por atualizar o perfil do paciente """
    paciente = get_object_or_404(Paciente, cpf=paciente_cpf)

    if request.method == 'POST':
        paciente_form = PacienteForm(request.POST, instance=paciente)
        if paciente_form.is_valid():
            paciente_form.save()

            return redirect('usuario_list', usuario_id=paciente.avaliador.id)

    else:
        paciente_form = PacienteForm(instance=paciente)
    context = {
        'paciente_form': paciente_form,
        'paciente': paciente,
        'footer_position' : 'absolute',
    }
    return render(request, 'conta/paciente_update.html', context)

@login_required
def paciente_delete(request, paciente_cpf):
    """ Esta view é responsável por deletar o paciente """
    paciente = get_object_or_404(Paciente, cpf=paciente_cpf)
    usuario_id = paciente.avaliador.id
    mensagem = ''
    time.sleep(1.5)
    try:
        paciente.delete()
        mensagem = 'Paciente apagado com sucesso'
        return redirect('usuario_list', usuario_id=usuario_id)
    except:
        context = {
            'mensagem': mensagem
        }
    return render(request, 'content.html', context)

@login_required
def realizar_avaliacao(request, paciente_cpf):
    """ Esta view é responsável por realizar a avaliação do paciente """
    paciente = get_object_or_404(Paciente, cpf=paciente_cpf)
    pontuacao = 0
    if request.method == 'POST':
        form = QuestionarioSarcopeniaForm(request.POST)

        if form.is_valid():
            dados_avaliacao = form.cleaned_data

            questionario = Questionario()
            questionario.paciente = paciente
            questionario.avaliador = paciente.avaliador
            questionario.data = timezone.now().date()
            questionario.respostas = dados_avaliacao
            questionario.save()

            dados_avaliacao.values()
            for resposta in dados_avaliacao.values():

                if int(resposta) <=2:
                    pontuacao += int(resposta)
                
                else:
                    if(paciente.sexo == 'F'):
                        if(int(resposta) < 33):
                            pontuacao += 0
                        else:
                            pontuacao +=10
                    else:
                        if(int(resposta) < 34):
                            pontuacao += 0
                        else:
                            pontuacao +=10

            if(pontuacao>=11):
                return render(request, 'conta/avaliacao_segunda_etapa.html', {'paciente': paciente, 'pontuacao': pontuacao, 'resultado': 'Alta probabilidade de sarcopenia'})


            return redirect('usuario_list', usuario_id=paciente.avaliador.id)
 
    else:
        form = QuestionarioSarcopeniaForm()
    
    context = {
        'form': form,
        'paciente': paciente,
    }

    return render(request, 'conta/realizar_avaliacao.html', context)
 
 
    context = {
        'paciente': paciente,
    }
    return render(resquest, 'conta/realizar_avaliacao.html', context)