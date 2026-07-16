from django.contrib import admin
from django.urls import path
from .views import listagem, detalhe
app_name='jogos'

urlpatterns = [
    path('', listagem, name='listagem'),
    path('<int:id>/', detalhe, name='detalhe')
]