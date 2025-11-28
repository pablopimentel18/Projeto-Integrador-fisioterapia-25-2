from django.shortcuts import render, get_object_or_404, redirect
from conta.models.usuario import Usuario
from conta.models.paciente import Paciente
from questionario.models.questionario import Questionario
from .forms import QuestionarioSegundaEtapaForm, QuestionarioTerceiraEtapaForm, UserForm, UsuarioForm, PacienteForm, QuestionarioSarcopeniaForm, QuestionarioQuartaEtapaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django import template
from django.template.defaultfilters import stringfilter
from django.utils import timezone
import time
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from io import BytesIO

register = template.Library()

@login_required
def exportar_diagnostico_pdf(request, questionario_id):
    questionario = get_object_or_404(Questionario, id=questionario_id)
    paciente = questionario.paciente
    respostas = questionario.respostas
    
    total_pontos = 0
    chaves_sarc_f = ['forca', 'ajuda_caminhada', 'levantar', 'subir', 'queda']
    
    for chave in chaves_sarc_f:
        valor = respostas.get(chave)
        if valor is not None and str(valor).isdigit():
            total_pontos += int(valor)

    context = {
        'paciente': paciente,
        'questionario': questionario,
        'avaliacao': questionario,
        'respostas': respostas,
        'diagnostico': questionario.diagnostico,
        'total_pontos': total_pontos,
        'now': timezone.localtime(timezone.now()),
    }

    html_string = render_to_string('conta/diagnostico_pdf.html', context)

    try:
        buffer = BytesIO()
        HTML(string=html_string, base_url=request.build_absolute_uri('/')).write_pdf(buffer)
        pdf = buffer.getvalue()
        buffer.close()

        nome_paciente = ''.join(c for c in paciente.nome if c.isalnum() or c in ['_','-']).replace(' ', '_')
        data_avaliacao = questionario.data.strftime('%d-%m-%Y')
        nome_arquivo = f'avaliacao_{nome_paciente}_{data_avaliacao}.pdf'

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{nome_arquivo}"'
        return response

    except Exception as e:
        print(f"ERRO AO GERAR PDF: {e}")
        return HttpResponse(f"Erro ao gerar PDF: {e}", status=500)

@register.filter(name='split')
@stringfilter
def split(string, sep):
    """Return the string split by sep.

    Example usage: {{ value|split:"/" }}
    """
    return string.split(sep)


def create_user(request):
    """ Esta view é responsável por criar um User """
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
            form_instante.tipo_usuario = form_usuario.cleaned_data['tipo_usuario']
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
        qtd_pacientes = Paciente.objects.count()


        if paciente_form.is_valid():
            pc = paciente_form.cleaned_data
            paciente = Paciente()
            paciente.id = (qtd_pacientes + 1)
            paciente.nome = pc['nome']
            paciente.email = pc['email']
            paciente.cpf = pc['cpf']
            paciente.numero_telefone = pc['numero_telefone']
            paciente.idade = pc['idade']
            paciente.sexo = pc['sexo']
            paciente.raca = pc['raca']
            paciente.estatura = pc['estatura']
            paciente.peso = pc['peso']
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
def paciente_update(request, paciente_id):
    """ Esta view é responsável por atualizar o perfil do paciente """
    paciente = get_object_or_404(Paciente, id=paciente_id)

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
def paciente_delete(request, paciente_id):
    """ Esta view é responsável por deletar o paciente """
    paciente = get_object_or_404(Paciente, id=paciente_id)
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
def tipo_avaliacao(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == 'POST':
        tipo = request.POST.get('tipo')

        questionario = Questionario.objects.create(
            paciente=paciente,
            avaliador=paciente.avaliador,
            data=timezone.now(),
            respostas={},
            tipo=tipo,
        )

        print("CRIADO QUESTIONARIO:", questionario.id, "TIPO:", questionario.tipo)

        return redirect('avaliar_primeira_etapa', questionario_id=questionario.id)

    context = {
        'paciente': paciente,
    }
    return render(request, 'conta/tipo_avaliacao.html', context)



@login_required
def primeira_etapa_avaliacao(request, questionario_id):
    """ Esta view é responsável por realizar a avaliação do paciente """

    questionario = get_object_or_404(Questionario, id=questionario_id)
    paciente = questionario.paciente

    print("ETAPA 1 - QUESTIONARIO", questionario.id, "TIPO:", questionario.tipo)

    pontuacao = 0
    if request.method == 'POST':
        form = QuestionarioSarcopeniaForm(request.POST)

        if form.is_valid():
            dados_avaliacao = form.cleaned_data
            questionario.respostas.update(dados_avaliacao)
            questionario.save()
            dados_avaliacao.values()
            for resposta in dados_avaliacao.values():

                if int(resposta) <=2:
                    pontuacao += int(resposta)
                
                else:
                    if(paciente.sexo == 'F'):
                        if(int(resposta) <= 33):
                            pontuacao += 10
                        else:
                            pontuacao +=0
                    else:
                        if(int(resposta) <= 34):
                            pontuacao += 10
                        else:
                            pontuacao +=0

            if(pontuacao>=11):
                questionario.save()
                resultado_texto = "Paciente Atingiu mais de 11 pontos.\nReferente à potencial diagnóstico de Sarcopenia!."

                messages.success(request, resultado_texto)
                return redirect('avaliar_segunda_etapa', questionario_id=questionario.id)

            questionario.diagnostico = 'Paciente sem sarcopenia.'
            questionario.save()

            resultado_texto = "Paciente Sem Sarcopenia"

            messages.success(request, resultado_texto)

            return redirect('diagnostico', questionario_id=questionario.id)
 
    else:
        form = QuestionarioSarcopeniaForm()
    
    context = {
        'form': form,
        'paciente': paciente,
    }
    return render(request, 'conta/primeira_etapa_avaliacao.html', context)

def segunda_etapa_avaliacao(request, questionario_id):
    """ Esta view é responsável por realizar a segunda etapa da avaliação do paciente """
    questionario = get_object_or_404(Questionario, id=questionario_id)
    paciente = questionario.paciente

    print("ETAPA 2 - QUESTIONARIO", questionario.id, "TIPO:", questionario.tipo)

    if request.method == 'POST':
        form = QuestionarioSegundaEtapaForm(request.POST)

        if form.is_valid():
            dados_avaliacao = form.cleaned_data
            questionario.respostas.update(dados_avaliacao)
            questionario.save()
            escolha = dados_avaliacao.get('segunda_etapa')
            valor = dados_avaliacao.get('valor_segunda_etapa')
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
                
                if valor < 15:
                    resultado = 'Desempenho funcional normal'
                else:
                    resultado = 'Desempenho funcional reduzido'
                    terceira = True
        
            if terceira:


                resultado_texto = "Paciente contém fraqueza, diagnóstico de provável Sarcopenia."

                messages.warning(request, resultado_texto)


                return redirect('avaliar_terceira_etapa', questionario_id=questionario.id)

            else:

                questionario.diagnostico = 'Paciente sem sarcopenia.'
                questionario.save()

                resultado_texto = "Paciente sem sarcopenia"

                messages.success(request, resultado_texto)
                return redirect('diagnostico', questionario_id=questionario.id)
 
    else:

        form = QuestionarioSegundaEtapaForm()
    
    context = {
        'form': form,
        'paciente': paciente,
    }
    resultado_texto = "Paciente Atingiu mais de 11 pontos.\nReferente à potencial diagnóstico de Sarcopenia!."

    messages.success(request, resultado_texto)
    return render(request, 'conta/segunda_etapa_avaliacao.html', context)

@login_required
def terceira_etapa_avaliacao(request, questionario_id):
    """ Esta view é responsável por realizar a terceira etapa da avaliação do paciente """
    questionario = get_object_or_404(Questionario, id=questionario_id)
    paciente = questionario.paciente

    print("ETAPA 3 - QUESTIONARIO", questionario.id, "TIPO:", questionario.tipo)

    if request.method == 'POST':
        form = QuestionarioTerceiraEtapaForm(request.POST)

        if form.is_valid():
            dados_avaliacao = form.cleaned_data
            questionario.respostas.update(dados_avaliacao)
            questionario.save()

            escolha = dados_avaliacao.get('terceira_etapa')
            valor = dados_avaliacao.get('valor_terceira_etapa')
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
                    
                    if questionario.tipo == 'N':
                        immea = ((0.244*paciente.peso) + (7.8 * (paciente.estatura/100.0)) - (0.098 * paciente.idade) + (raca -3.3))/((paciente.estatura/100)*(paciente.estatura/100))
                        print("USANDO EQUAÇÃO NORMAL (F), IMMEA =", immea)
                    else:
                        immea = ((0.244*paciente.peso) + (7.8 * (paciente.estatura/100)) - (0.098 * paciente.idade) + (raca -3.3))/(paciente.peso)
                        print("USANDO EQUAÇÃO OBESO (F), IMMEA =", immea)

                    if immea < 6.4:
                        resultado = 'Baixa massa muscular esquelética dos membros inferiores pelo IMMEA'
                        quarta = True
                    else:
                        resultado = 'Massa muscular esquelética dos membros inferiores normal pelo IMMEA'
                else:
                    if questionario.tipo == 'N':    
                        immea = ((0.244*paciente.peso) + (7.8 * (paciente.estatura/100)) + (6.6 * 1) - (0.098 * paciente.idade) + (raca -3.3))/((paciente.estatura/100)*(paciente.estatura/100))
                        print("USANDO EQUAÇÃO NORMAL (M), IMMEA =", immea)
                    else:
                        immea = ((0.244*paciente.peso) + (7.8 * (paciente.estatura/100)) + (6.6 * 1) - (0.098 * paciente.idade) + (raca -3.3))/(paciente.peso)
                        print("USANDO EQUAÇÃO OBESO (M), IMMEA =", immea)
                    if immea < 8.9:
                        resultado = 'Baixa massa muscular esquelética dos membros inferiores pelo IMMEA'
                        quarta = True
                    else:
                        resultado = 'Massa muscular esquelética dos membros inferiores normal pelo IMMEA'

            
            if quarta:

                resultado_texto = "Paciente contém baixa massa muscular, diagnóstico de provável Sarcopenia."
                messages.warning(request, resultado_texto)
                return redirect('avaliar_quarta_etapa', questionario_id=questionario.id)    

        questionario.diagnostico = 'Provável sarcopenia'
        questionario.save()

        resultado_texto = "Provável Sarcopenia"

        messages.success(request, resultado_texto)

        return redirect('diagnostico', questionario_id=questionario.id)
 
    else:
        form = QuestionarioTerceiraEtapaForm()
    
    context = {
        'paciente': paciente,
        'form': form,
    }

    return render(request, 'conta/terceira_etapa_avaliacao.html', context)

@login_required
def quarta_etapa_avaliacao(request, questionario_id):
    """ Esta view é responsável por realizar a quarta etapa da avaliação do paciente """
    questionario = get_object_or_404(Questionario, id=questionario_id)
    paciente = questionario.paciente


    if request.method == 'POST':
        form = QuestionarioQuartaEtapaForm(request.POST)
    
        if form.is_valid():
            dados_avaliacao = form.cleaned_data
            questionario.respostas.update(dados_avaliacao)
            questionario.save()

            tempo = dados_avaliacao.get('valor_quarta_etapa')
            if((4/tempo) <= 0.8):
                grave=True
                questionario.diagnostico = 'Sarcopenia grave.'
                resultado_texto = "Diagnóstico de sarcopenia grave"
            else:
                grave=False
                questionario.diagnostico = 'Sarcopenia confirmada.'
                resultado_texto = "Sarcopenia confirmada"

            questionario.save()
            messages.success(request, resultado_texto)
            return redirect('diagnostico', questionario_id=questionario.id)

        return redirect('diagnostico', questionario_id=questionario.id) 

    else: 
        form = QuestionarioQuartaEtapaForm()


    context = {
        'paciente': paciente,
        'form': form,
    }

    return render(request, 'conta/quarta_etapa_avaliacao.html', context)

@login_required
def diagnostico(request, questionario_id):
    """ Esta view é responsável por exibir o diagnóstico final do paciente """
    questionario = get_object_or_404(Questionario, id=questionario_id)
    paciente = questionario.paciente
    respostas = questionario.respostas
    diagnostico = questionario.diagnostico
    grave = False

    if 'valor_quarta_etapa' in respostas:
        tempo = respostas.get('valor_quarta_etapa')
        if((4/tempo) <= 0.8):
            grave=True


    print(questionario.tipo)

    context = {
        'paciente': paciente,
        'respostas': respostas,
        'diagnostico': diagnostico,
    }

    return render(request, 'conta/diagnostico.html', context)

@login_required
def questionario_list(request, paciente_id):
    """ Esta view é responsável por listar todos os questionarios de um paciente específico """
    paciente = get_object_or_404(Paciente, id=paciente_id)

    Questionario.objects.filter(
        paciente=paciente, 
        diagnostico__isnull=True
    ).delete()

    questionarios = Questionario.objects.filter(paciente=paciente).order_by('-data')

    context = {
        'questionarios': questionarios,
        'paciente': paciente,
    }
    return render(request, 'conta/questionario_list.html', context)
	
@login_required
def aluno_list(request):
    """ 
    Lista todos os Avaliadores (tipo 'A') e permite pesquisa por nome. 
    Acesso restrito a professores (tipo 'P').
    """
    search_query = request.GET.get('q')
    
    try:
        if request.user.usuario.tipo_usuario == 'P':
            
            alunos_avaliadores = Usuario.objects.filter(tipo_usuario='A').select_related('user').order_by('nome')
            
            if search_query:
                alunos_avaliadores = alunos_avaliadores.filter(nome__icontains=search_query)

            context = {
                'alunos': alunos_avaliadores,
                'search_query': search_query, 
            } 
        else:
            return HttpResponse("Acesso negado. Apenas professores administradores podem acessar esta página.", status=403)
        
    except Usuario.DoesNotExist:
        return HttpResponse("Acesso negado. Usuário não encontrado.", status=403)
    
    return render(request, 'conta/aluno_list.html', context)

@login_required
def aluno_avaliacoes(request, usuario_id):
    """ Esta view é responsável por listar todas as avaliações de um aluno específico """
    aluno = get_object_or_404(Usuario, pk=usuario_id)

    if aluno.tipo_usuario != 'A':
        return HttpResponse("Acesso negado. O usuário especificado não é um aluno avaliador.", status=403)
    else:
        pacientes = Paciente.objects.filter(avaliador=aluno)
        avaliacoes = Questionario.objects.filter(paciente__in=pacientes).order_by('-data')

        context = {
            'aluno': aluno,
            'avaliacoes': avaliacoes,
        }
    return render(request, 'conta/aluno_avaliacoes.html', context)

@login_required
def relatorios_gerais(request):
    """ Exibe a página 'Em Desenvolvimento' para a área de relatórios. """
        
    return render(request, 'conta/relatorio_professor.html') 