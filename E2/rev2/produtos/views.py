from django.shortcuts import render

# Create your views here.
produtos=[
    {
        'id':1,
        'nome': 'Notebook',
        'categoria': 'Informática',
        'preco': 3000,
        'descricao': 'Notebook gamer massa',
    },

    {
        'id':2,
        'nome': 'Mikasa V200W',
        'categoria': 'Esportes',
        'preco': 600,
        'descricao': 'Bola de vôlei top',
    },

    {
        'id':3,
        'nome': 'Sky Elite 3',
        'categoria': 'Esportes',
        'preco': 900,
        'descricao': 'Tênis de vôlei top',
    },
]

def listagem(request):
    return render(request, 'produtos/listagem.html', {'produtos': produtos})

def detalhe(request, id):
    produto = None
    for p in produtos:
        if p['id'] == id:
            produto = p
            break
    return render(request,'produtos/detalhe.html',{'produto':produto})
