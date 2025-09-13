from django.shortcuts import render, get_object_or_404
from conta.models.usuario import *

def index(request):
    """ view para url base do projeto """
    context = {
        'footer_position' : 'absolute',
    }
    return render(request, 'content.html', context)