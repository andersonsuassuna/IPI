from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def minha_view(request):
    return HttpResponse("Esta é minha view!")

def produtos_view(request):
    def produtos_view(request):
        itens = ["Notebook", "Mouse", "Teclado", "Monitor"]
        contexto = {
        "title": "Loja Tech",
        "itens_list": itens,
        "total": len(itens)
        }
        return render(request, 'produtos.html', contexto)

def vitrine(request):
   contexto = {
        'titulo': 'Vitrine', # string
        'total': 5, # número
        'promocao': True, # booleano
        'produtos': [
            {'nome': 'Camiseta', 'preco': 39.90},
            {'nome': 'Calça Jeans', 'preco': 129.90},
            {'nome': 'Boné', 'preco': 45.00},
            {'nome': 'Tênis', 'preco': 219.90},
            {'nome': 'Meia', 'preco': 59.90},
        ]
   }
   return render(request, 'vitrine.html', contexto)

def produto_detalhe_view(request, produto_id):
 contexto = {
   "title": "Loja Tech",
   "produto_id": produto_id,
   "nome": f"Produto {produto_id}",
   "descricao": f"Descrição do produto {produto_id}",
   "preco": f"R$ {produto_id * 10:.2f}"
 }
 return render(request, 'produto_detalhe_view.html', contexto)

def sobre_nos(request):
   contexto = {
       'loja': 'Fashion Store',
       'fundacao': 2020,
       'servicos': [
           'Entrega rápida',
           'Troca grátis',
           'Suporte 24h',
       ],
   }
   return render(request,
       'sobre.html', contexto)
