from django.db import models
import random


class CodigoProfessor(models.Model):
    codigo = models.CharField(max_length=10, unique=True, blank=True, null=True)

    @staticmethod
    def gerar_novo_codigo():
        return f"{random.randint(1000, 9999)}"

    @classmethod
    def get_atual(cls):
        """
        Retorna o registro de código (id=1). Se não existir ou não tiver código,
        cria/gera um novo e salva.
        """
        obj, created = cls.objects.get_or_create(id=1)
        if created or not obj.codigo:
            obj.codigo = cls.gerar_novo_codigo()
            obj.save()
        return obj

    def __str__(self):
        return self.codigo or ""