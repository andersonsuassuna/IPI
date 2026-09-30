from django.contrib import admin
from django.urls import path
from . import views

app_name = "noticias"
urlpatterns = [
 path("categoria/criar/", views.categoria_create_view, name="categoria_create"),
]
