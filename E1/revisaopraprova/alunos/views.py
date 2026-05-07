from django.shortcuts import render

# Create your views here.
def home_alunos(request):
    return render(request, 'home_alunos.html')