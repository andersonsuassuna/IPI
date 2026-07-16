from django.shortcuts import render

# Create your views here.
jogos=[
    {
        'id':1,
        'titulo': 'God of war',
        'desenvolvedora': 'Santa Monica',
        'ano': 2018,
        'genero': 'RPG',
    },

    {
        'id':2,
        'titulo': 'Super Mario 64',
        'desenvolvedora': 'Nintendo',
        'ano': 1995,
        'genero': 'Plataforma',
    },

    {
        'id':3,
        'titulo': 'GTA VI',
        'desenvolvedora': 'Rockstar',
        'ano': 2026,
        'genero': 'RP',
    },

    {
        'id':4,
        'titulo': 'Red Dead Redemption',
        'desenvolvedora': 'Rockstar',
        'ano': 2018,
        'genero': 'Ação',
    },

    {
        'id':5,
        'titulo': 'Geometry Dash',
        'desenvolvedora': 'Robtop',
        'ano': 2012,
        'genero': 'Plataforma',
    },
]

def listagem(request):
    return render(request, 'jogos/listagem.html', {'jogos':jogos})

def detalhe(request,id):
    jogo=None
    for j in jogos:
        if j['id']==id:
            jogo=j
    return render(request, 'jogos/detalhe.html', {'jogo':jogo})