from django.shortcuts import render

# Create your views here.
produtos_db=[
    {'id':1, 'nome':'Notebook','preco':3000},
    {'id':2, 'nome':'Mikasa V200W', 'preco': 600},
]

def listagem(request):
    return render(request, 'produtos/listagem.html', {'produtos' : produtos_db})

def detalhe(request):
    for i in produtos_db:
        produto_selecionado=i
    return render(request, 'produtos/detalhe.html', {'produto': produto_selecionado})