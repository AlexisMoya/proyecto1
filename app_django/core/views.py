from django.shortcuts import render, redirect
from django.template import loader
from .models import Libro
from .forms import LibroForm

# Create your views here.
def home(request):
    libros = Libro.objects.all()
    datos  = {
        'libros' : libros
    } 
    return render(request, 'core/home.html', datos)

def form_libro(request):
    datos = {
        'form': LibroForm()
    }
    if request.method == 'POST':
        formulario = LibroForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados Correctamente"
    return render(request, 'core/form_libro.html ', datos)

def form_mod_libro(request, id):
    libro = Libro.objects.get(isbn=id)
    datos = {
        'form': LibroForm(instance=libro)
    }
    return render(request, 'core/form_mod_libro.html', datos)

    if request.method== 'POST':
        formulario = LibroForm(data=request.POST,instance=libro)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados Correctamente"
    return render(request, 'core/form_mod_libro.html' , datos)

def form_del_libro(request, id):
    libro = Libro.objects.get(isbn=id)
    libro.delete()
    return redirect(to="home")
            
