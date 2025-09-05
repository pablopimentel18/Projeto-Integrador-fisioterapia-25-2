from django.shortcuts import render, get_object_or_404
from conta.models.usuario import *

def index(request):
    """ view para url base do projeto """
    context = {
        
    }
    return render(request, 'content.html', context)