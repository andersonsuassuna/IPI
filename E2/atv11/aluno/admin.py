from django.contrib import admin

# Register your models here.
from .models import Aluno
admin.site.register(Aluno)

from .models import Filme
admin.site.register(Filme)