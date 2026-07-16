from django.shortcuts import render

# Create your views here.
servicos=[
    {
        'id':1,
        'nome_servico': 'Site',
        'responsavel': 'João',
        'tempo_estimado': '10 dias',
        'requisitos': 'Logo',
    },

    {
        'id':1,
        'nome_servico': 'Loja',
        'responsavel': 'Maria',
        'tempo_estimado': '4 meses',
        'requisitos': 'Espaço',
    },

    {
        'id':1,
        'nome_servico': 'Água',
        'responsavel': 'Marcos',
        'tempo_estimado': '1 hora',
        'requisitos': 'Local para entrega',
    },
]

def listagem(request):
    return render(request, 'servicos/listagem.html', {'servicos': servicos})

def detalhe(request, id):
    servico = None
    for s in servicos:
        if s['id'] == id:
            servico = s
            break
    return render(request,'servico/detalhe.html',{'servico':servico})
