from django.shortcuts import render


def menu_view(request):
    contexto = {
        'nome_loja': 'Geek Burger',
        'loja_aberta': True,
        'promocao_do_dia': 'Combo Gamer com 20% de desconto!',
        'lanches': [
            'Cheeseburger',
            'Bacon Duplo',
            'Vegano',
            'Batata Rústica'
        ]
    }

    return render(request, 'cardapio/cardapio.html', contexto)