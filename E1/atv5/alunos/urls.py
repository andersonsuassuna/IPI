from django.contrib import admin
from django.urls import path
from .views import lista_alunos, novo_alunos, detalhe_alunos

app_name='alunos'

urlpatterns = [
    path('lista/', lista_alunos, name='lista'),
    path('novo/', novo_alunos, name='novo'),
    path('detalhe/', detalhe_alunos, name='detalhe')
]
