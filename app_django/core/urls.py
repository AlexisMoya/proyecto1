from django.urls import path
from .views import home, form_libro, form_mod_libro, form_mod_libro

urlpatterns = [
    path('', home, name="home"),
    path('form-libro', form_libro, name="form_libro"),
    path('form-mod-libro/<id>', form_mod_libro, name="form_mod_vehiculo"),
    
    
]


 