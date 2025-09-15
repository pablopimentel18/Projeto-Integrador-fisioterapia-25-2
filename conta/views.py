from django.shortcuts import render, get_object_or_404, redirect
from conta.models.usuario import *
from .forms import UserForm, UsuarioForm
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
        return redirect('logout')
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
def usuario_list(request):
    """ Esta view é responsável por listar todos os usuario que estão cadastrados no banco de dados """
    usuarios = Usuario.objects.all()
    context = {
        'usuarios': usuarios
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
