from django.contrib import admin
from .models import Usuario
from .models.paciente import Paciente
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Paciente)
