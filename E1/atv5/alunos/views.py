from django.shortcuts import render

# Create your views here.

def lista_alunos(request):
    return render(request, '../templates/alunos/lista_alunos.html')

def novo_alunos(request):
    return render(request, '../templates/alunos/novo_alunos.html')

def detalhe_alunos(request):
    return render(request, '../templates/alunos/detalhe_alunos.html')