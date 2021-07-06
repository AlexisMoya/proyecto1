from django.db import models

#Modelo de categoria
class Categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=50, verbose_name='NombreCategoria')

    def __str__(self):
        return self.nombreCategoria

# Modelo para la bibioteca
class Libro(models.Model):
    isbn =   models.IntegerField(max_length=3,primary_key=True, verbose_name='ISBN')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    autor =  models.CharField(max_length=20, verbose_name='Autor')
    descripcion = models.CharField(max_length=200, null=True, blank=True, verbose_name='Descripcion')
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
