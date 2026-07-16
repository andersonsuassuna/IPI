from django.urls import path
from . import views

urlpatterns = [
    path('', views.listagem, name='lista_produtos'),
    path('<int:id>/', views.detalhe, name='detalhe_produto'),
]