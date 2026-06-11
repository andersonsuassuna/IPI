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
       'total': 3, # número
       'produtos': [
           'Camiseta',
           'Calça',
           'Boné',
       ], # lista
       'promocao': True, # booleano
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
