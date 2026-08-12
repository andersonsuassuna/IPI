from django.shortcuts import render

# Create your views here.
roupas=[
    {
        'id':1,
        'nome': 'Camisa Polo',
        'marca': 'Acostamento',
        'preco': 120,
        'tamanho': 'M',
    },

    {
        'id':2,
        'nome': 'Calça Jeans',
        'marca': 'Cruzada',
        'preco': 200,
        'tamanho': 'M',
    },

    {
        'id':3,
        'nome': 'Camisa de esporte',
        'marca': 'Adidas',
        'preco': 80,
        'tamanho': 'P',
    },

    {
        'id':4,
        'nome': 'Camisa de time',
        'marca': 'Nike',
        'preco': 300,
        'tamanho': 'G',
    },

    {
        'id':5,
        'nome': 'Shorts tactel',
        'marca': 'Lupo',
        'preco': 100,
        'tamanho': 'M',
    },
]

def listagem(request):
    return render(request, 'roupas/listagem.html', {'roupas':roupas})

def detalhe(request,id):
    roupa=None
    for r in roupas:
        if r['id']==id:
            roupa=r
    return render(request, 'roupas/detalhe.html', {'roupa':roupa})