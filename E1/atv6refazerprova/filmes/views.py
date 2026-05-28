from django.shortcuts import render

# Create your views here.
def detalhe(request):
    return render(request, '../templates/filmes/detalhe.html')

def lista(request):
    return render(request, '../templates/filmes/lista.html')