from django.contrib import admin
from .models.questionario import Questionario, Pergunta, Resposta

@admin.register(Questionario)
class QuestionarioAdmin(admin.ModelAdmin):
    list_display = ("id", "paciente", "data_criacao")
    search_fields = ("paciente__nome",)

@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ("ordem", "texto")
    ordering = ("ordem",)

@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ("questionario", "pergunta", "nota_intensidade")
    search_fields = ("questionario__paciente__nome",)