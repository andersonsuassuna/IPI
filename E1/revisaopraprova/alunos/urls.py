from django.contrib import admin
from django.urls import path
from .views import home_alunos

app_name='alunos'

urlpatterns = [
    path('', home_alunos, name='home_alunos'),
]
