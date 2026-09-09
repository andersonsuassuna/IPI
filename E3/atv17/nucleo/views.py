from django.shortcuts import render, get_object_or_404
from .models import Projeto

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'lista.html', {'projetos': projetos})

def detalhes_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    return render(request, 'detalhes.html', {'projeto': projeto})