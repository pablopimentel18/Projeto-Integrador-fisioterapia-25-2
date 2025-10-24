from django.shortcuts import render, get_object_or_404, redirect
from conta.models.usuario import *
from conta.models.paciente import Paciente
from questionario.models.questionario import Questionario
from .forms import QuestionarioSegundaEtapaForm, QuestionarioTerceiraEtapaForm, UserForm, UsuarioForm, PacienteForm, QuestionarioSarcopeniaForm, QuestionarioQuartaEtapaForm
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
def tipo_avaliacao(request, paciente_cpf): 
    """ Esta view é responsável por escolher o tipo de avaliação do paciente """
    paciente = get_object_or_404(Paciente, cpf=paciente_cpf)
    context = {
        'paciente': paciente,
    }
    return render(request, 'conta/tipo_avaliacao.html', context)


@login_required
def primeira_etapa_avaliacao(request, paciente_cpf):
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
                return redirect('avaliar_segunda_etapa', paciente_cpf=paciente.cpf)

            questionario.diagnostico = 'Paciente sem sarcopenia'
            questionario.save()
            return redirect('diagnostico', paciente_cpf=paciente.cpf)
 
    else:
        form = QuestionarioSarcopeniaForm()
    
    context = {
        'form': form,
        'paciente': paciente,
    }

    return render(request, 'conta/primeira_etapa_avaliacao.html', context)

def segunda_etapa_avaliacao(request, paciente_cpf):
    """ Esta view é responsável por realizar a segunda etapa da avaliação do paciente """
    paciente = get_object_or_404(Paciente, cpf=paciente_cpf)
    questionario = Questionario.objects.filter(paciente=paciente).latest('data')

    if request.method == 'POST':
        form = QuestionarioSegundaEtapaForm(request.POST)

        if form.is_valid():
            dados_avalicao = form.cleaned_data
            questionario.respostas.update(dados_avalicao)
            questionario.save()
            escolha = dados_avalicao.get('segunda_etapa_avaliacao')
            valor = dados_avalicao.get('valor_segunda_etapa')
            terceira = False

            if escolha == 'Forca Preensar':
                
                if paciente.sexo == 'F':
                    if valor < 16:
                        resultado = 'Baixa força de preensão manual'
                        terceira = True
                    else:
                        resultado = 'Força de preensão manual normal'
                        
                else:
                    if valor < 27:
                        resultado = 'Baixa força de preensão manual'
                        terceira = True
                    else:
                        resultado = 'Força de preensão manual normal'

            else : 
                
                if valor > 15:
                    resultado = 'Desempenho funcional normal'
                else:
                    resultado = 'Desempenho funcional reduzido'
                    terceira = True
        
            if terceira:
                return redirect('avaliar_terceira_etapa', paciente_cpf=paciente.cpf)

            questionario.diagnostico = 'Paciente sem sarcopenia'
            questionario.save()
            return redirect('usuario_list', usuario_id=paciente.avaliador.id)
 
    else:
        form = QuestionarioSegundaEtapaForm()
    
    context = {
        'form': form,
        'paciente': paciente,
    }

    return render(request, 'conta/segunda_etapa_avaliacao.html', context)

@login_required
def terceira_etapa_avaliacao(request, paciente_cpf):
    """ Esta view é responsável por realizar a terceira etapa da avaliação do paciente """
    paciente = get_object_or_404(Paciente, cpf=paciente_cpf)
    questionario = Questionario.objects.filter(paciente=paciente).latest('data')

    if request.method == 'POST':
        form = QuestionarioTerceiraEtapaForm(request.POST)

        if form.is_valid():
            dados_avalicao = form.cleaned_data
            questionario.respostas.update(dados_avalicao)
            questionario.save()

            escolha = dados_avalicao.get('terceira_etapa')
            valor = dados_avalicao.get('valor_terceira_etapa')
            quarta = False 

            if escolha == 'MMEA':
                
                if paciente.sexo == 'F':
                    if valor < 20:
                        resultado = 'Baixa massa muscular esquelética dos membros inferiores'
                        quarta = True
                    else:
                        resultado = 'Massa muscular esquelética dos membros inferiores normal'
                        
                else:
                    if valor < 15:
                        resultado = 'Baixa massa muscular esquelética dos membros inferiores'
                        quarta = True
                    else:
                        resultado = 'Massa muscular esquelética dos membros inferiores normal'

            else : 

                if paciente.raca == 'B':
                    raca = 0
                elif paciente.raca == 'P':
                    raca = 1.4
                else:
                    raca = -1.2

                if paciente.sexo == 'F':

                    immea = ((0.244*paciente.peso) + (7.8 * (paciente.estatura/100)) - (0.098 * paciente.idade) + (raca -3.3))/((paciente.estatura/100)*(paciente.estatura/100))

                    if immea < 6.4:
                        resultado = 'Baixa massa muscular esquelética dos membros inferiores pelo IMMEA'
                        quarta = True
                    else:
                        resultado = 'Massa muscular esquelética dos membros inferiores normal pelo IMMEA'
                else:
                    immea = ((0.244*paciente.peso) + (7.8 * (paciente.estatura/100)) + (6,6 * 1) - (0.098 * paciente.idade) + (raca -3.3))/((paciente.estatura/100)*(paciente.estatura/100))
                    if immea < 8.9:
                        resultado = 'Baixa massa muscular esquelética dos membros inferiores pelo IMMEA'
                        quarta = True
                    else:
                        resultado = 'Massa muscular esquelética dos membros inferiores normal pelo IMMEA'

            
            if quarta:
                return redirect('avaliar_quarta_etapa', paciente_cpf=paciente.cpf)    

        questionario.diagnostico = 'Provável sarcopenia'
        questionario.save()
        return redirect('usuario_list', usuario_id=paciente.avaliador.id)

 
    else:
        form = QuestionarioTerceiraEtapaForm()
    
    context = {
        'paciente': paciente,
        'form': form,
    }

    return render(request, 'conta/terceira_etapa_avaliacao.html', context)

@login_required
def quarta_etapa_avaliacao(request, paciente_cpf):
    """ Esta view é responsável por realizar a quarta etapa da avaliação do paciente """
    paciente = get_object_or_404(Paciente, cpf=paciente_cpf)
    questionario = Questionario.objects.filter(paciente=paciente).latest('data')


    if request.method == 'POST':
        form = QuestionarioQuartaEtapaForm(request.POST)
    
        if form.is_valid():
            dados_avalicao = form.cleaned_data
            questionario.respostas.update(dados_avalicao)
            questionario.save()

            tempo = dados_avalicao.get('valor_quarta_etapa')
            if((4/tempo) <= 0.8):
                grave=True
                questionario.diagnostico = 'Sarcopenia grave'
            else:
                grave=False
                questionario.diagnostico = 'Sarcopenia'

            questionario.save()
            return redirect('diagnostico', paciente_cpf=paciente.cpf)

        return redirect('usuario_list', usuario_id=paciente.avaliador.id)   

    else: 
        form = QuestionarioQuartaEtapaForm()


    context = {
        'paciente': paciente,
        'form': form,
    }

    return render(request, 'conta/quarta_etapa_avaliacao.html', context)

@login_required
def diagnostico(request, paciente_cpf):
    """ Esta view é responsável por exibir o diagnóstico final do paciente """
    paciente = get_object_or_404(Paciente, cpf=paciente_cpf)
    questionario = Questionario.objects.filter(paciente=paciente).latest('data')
    respostas = questionario.respostas
    diagnostico = questionario.diagnostico
    grave = False

    if 'valor_quarta_etapa' in respostas:
        tempo = respostas.get('valor_quarta_etapa')
        if((4/tempo) <= 0.8):
            grave=True


    context = {
        'paciente': paciente,
        'respostas': respostas,
        'diagnostico': diagnostico,
    }

    return render(request, 'conta/diagnostico.html', context)

@login_required
def questionario_list(request, paciente_cpf):
    """ Esta view é responsável por listar todos os questionarios de um paciente específico """
    paciente = get_object_or_404(Paciente, cpf=paciente_cpf)
    questionarios = Questionario.objects.filter(paciente=paciente).order_by('-data')
    context = {
        'questionarios': questionarios,
        'paciente': paciente,
    }
    return render(request, 'conta/questionario_list.html', context)