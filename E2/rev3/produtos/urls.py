from django.contrib import admin
from django.urls import path

from .views import listagem, detalhe

urlpatterns = [
    path('', listagem, name='listagem_produtos'),
    path('<int:id>/', detalhe, name='detalhe_produtos')
]
