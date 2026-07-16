from django.shortcuts import render

# Create your views here.
servicos=[
    {
        'id':1,
        'nome':'Água',
        'responsavel':'João',
        'tempo_estimado':'1 hora',
        'requisitos':'Informar local',
    },

    {
        'id':2,
        'nome':'Energia',
        'responsavel':'Marcos',
        'tempo_estimado':'30 minutos',
        'requisitos':'Pagar a conta',
    },
]

def listagem(request):
    return render(request, 'servicos/listagem.html', {'servicos':servicos})

def detalhe(request,id):
    servico=None
    for s in servicos:
        if s['id'] == id:
            servico = s
            break
    return render(request, 'servicos/listagem.html', {'servico':servico})