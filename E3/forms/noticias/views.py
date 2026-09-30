from django.shortcuts import render
from . import models

# Create your views here.
from . import forms
def categoria_create_view(request):
   if request.method == "POST":
       form = forms.CategoriaForm(request.POST)
       if form.is_valid():
           nome_form = form.cleaned_data["nome"]
           models.Categoria.objects.create(
               nome=nome_form
           )
           return redirect("noticias:categorias")
   else:
       form = forms.CategoriaForm()
   return render(request, "categoria/form.html", {
       "form": form,
   })
