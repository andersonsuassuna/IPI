from django.contrib import admin
from django.urls import path
from .views import detalhe, lista

app_name='filmes'

urlpatterns = [
    path('detalhe/', detalhe, name='detalhe'),
    path('lista/', lista, name='lista')
]
