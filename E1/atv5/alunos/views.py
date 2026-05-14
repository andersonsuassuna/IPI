from django.shortcuts import render

# Create your views here.
def home_alunos(request):
    return render(request, 'home_alunos.html')

def lista_alunos(request):
    return render(request, 'lista_alunos.html')

def novo_alunos(request):
    return render(request, 'novo_alunos.html')

def detalhe_alunos(request):
    return render(request, 'detalhe_alunos.html')