from django import forms
from django.forms import ModelForm 
from .models import Libro
 
#creamos nuestra clase para el formulario desde la base de datos
class LibroForm(ModelForm):

    class Meta:
        model = Libro
        fields =('isbn','nombre','autor','descripcion','Categoria')