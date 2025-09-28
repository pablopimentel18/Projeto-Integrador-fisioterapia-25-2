from .base import BaseModel
from django.db import models
from conta.models.paciente import Paciente

class Questionario(BaseModel):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="questionarios")

    def __str__(self):
        return self.paciente.nome if self.paciente else f"Questionario #{self.pk}"


class Pergunta(BaseModel):
    texto = models.CharField(max_length=512)
    ordem = models.PositiveIntegerField(default=0, help_text="Ordem da pergunta no questionario")

    class Meta:
        ordering = ["ordem"]

    def __str__(self):
        return f"{self.ordem}. {self.texto}"


class Resposta(BaseModel):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE, related_name="respostas")
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name="respostas")

    resposta_texto = models.TextField(blank=True, null=True)
    nota_intensidade = models.PositiveSmallIntegerField(
        blank=True, null=True,
        help_text="Opcional: nota de intensidade (ex: 0-10)"
    )

    def __str__(self):
        return f"Resp. Q#{self.questionario_id} - P#{self.pergunta_id}"
