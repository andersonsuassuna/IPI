from django.contrib import admin
from django.urls import path
from .views import home_aluno

app_name='aluno'

urlpatterns = [
    path('', home_aluno, name='home_aluno'),
]
