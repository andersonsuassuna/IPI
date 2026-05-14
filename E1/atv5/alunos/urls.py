from django.contrib import admin
from django.urls import path
from .views import home_alunos, lista_alunos, novo_alunos, detalhe_alunos

app_name='alunos'

urlpatterns = [
    path('', home_alunos, name='home_alunos'),
    path('lista/', lista_alunos, name='lista'),
    path('novo/', novo_alunos, name='novo'),
    path('detalhe/', detalhe_alunos, name='detalhe')
]
