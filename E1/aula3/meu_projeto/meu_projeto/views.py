from django.shortcuts import render # importando render

def viewnova(request): # criando view
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')