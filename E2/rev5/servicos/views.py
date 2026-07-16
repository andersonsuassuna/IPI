from django.shortcuts import render

# Create your views here.
servicos=[
    {
        'id':1,
        'nome':"Água",
        'responsavel':"João",
        'tempo':'1 hora',
        'requisitos':"Local da entrega",
    },
]

def listagem(request):
    return render(request, 'servicos/listagem.html', {'servicos':servicos})

def detalhe(request,id):
    servico=None
    for s in servicos:
        if s['id']==id:
            servico=s
            break
    return render(request, 'servicos/detalhe.html', {'servico':servico})