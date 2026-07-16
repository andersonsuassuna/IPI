from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('core.urls')),
    path('produtos/', include('produtos.urls')),
    path('servicos/', include('servicos.urls')),
]
