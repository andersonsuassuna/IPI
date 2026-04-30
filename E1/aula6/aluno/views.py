from django.shortcuts import render

# Create your views here.
def home_aluno(request):
    return render(request, 'aluno/home_aluno.html')

def lista_alunos(request):
    return render(request, 'aluno/lista_alunos.html')