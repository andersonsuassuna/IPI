from django.contrib import admin
from django.urls import path
from .views import listagem, detalhe
app_name='servicos'

urlpatterns = [
    path('', listagem, name='listagem_servicos'),
    path('<int:id>/', detalhe, name='detalhe_servicos')
]