from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.minha_view, name='nome'),
    path('templates/', views.produtos_view, name='templates'),
    path('vitrine/', views.vitrine, name='vitrine'),
    path('produtos/<int:produto_id>/', views.produto_detalhe_view, name='produto_detalhe'),
    path('sobre/', views.sobre_nos, name='sobre'),
]