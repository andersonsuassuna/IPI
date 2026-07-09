from django.shortcuts import render

# Dados Hardcoded
PRODUTOS_DB = [
    {"id": 1, "nome": "Notebook Pro", "categoria": "Eletrônicos", "preco": 5500.00, "descricao": "Notebook de alta performance com 16GB de RAM e 512GB SSD."},
    {"id": 2, "nome": "Cadeira Ergonômica", "categoria": "Móveis", "preco": 1200.00, "descricao": "Cadeira ajustável com suporte lombar de malha respirável."},
    {"id": 3, "nome": "Monitor UltraWide", "categoria": "Eletrônicos", "preco": 2300.00, "descricao": "Monitor 34 polegadas com taxa de atualização de 144Hz."},
    {"id": 4, "nome": "Teclado Mecânico", "categoria": "Periféricos", "preco": 450.00, "descricao": "Teclado com switches azuis e iluminação RGB customizável."},
    {"id": 5, "nome": "Mouse sem fio", "categoria": "Periféricos", "preco": 200.00, "descricao": "Mouse com bateria de longa duração e sensor de alta precisão."}
]

def listagem(request):
    return render(request, 'produtos/listagem.html', {'produtos': PRODUTOS_DB})

def detalhe(request, id):
    # Busca o produto pelo ID na lista
    produto_selecionado = next((p for p in PRODUTOS_DB if p["id"] == id), None)
    return render(request, 'produtos/detalhe.html', {'produto': produto_selecionado})