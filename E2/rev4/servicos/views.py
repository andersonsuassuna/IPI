from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
servicos=[
    {
        'id':1,
        'nome':'Água',
        'responsável':'Marlon',
        'tempo':'1 hora',
        'requisitos':'Local de entrega',
    },
]

def listagem(request):
    return render(request, 'servicos/listagem.html', {'servicos':servicos})

def detalhe(request, id):
    servico=None
    for s in servicos:
        if s['id']==id:
            servico=s
            break
    return render(request, 'servicos/detalhe.html', {'servico': servico})