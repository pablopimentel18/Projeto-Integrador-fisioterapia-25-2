from django.contrib import admin
from conta.models.usuario import Usuario
from conta.models.paciente import Paciente
from conta.models.codigo_professor import CodigoProfessor
from questionario.models.questionario import Questionario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "nome", "tipo_usuario", "email")
    search_fields = ("nome", "email", "nome_de_usuario")


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "cpf", "idade", "sexo", "avaliador")
    search_fields = ("nome", "cpf")
    list_filter = ("sexo", "raca")


@admin.register(Questionario)
class QuestionarioAdmin(admin.ModelAdmin):
    list_display = ("id", "paciente", "avaliador", "data", "tipo", "diagnostico")
    search_fields = ("paciente__nome", "avaliador__nome")


@admin.register(CodigoProfessor)
class CodigoProfessorAdmin(admin.ModelAdmin):
    list_display = ("id", "codigo")
