from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_projetos, name='lista_projetos'),
    path('projeto/<int:id>/', views.detalhes_projeto, name='detalhes_projeto'),
]