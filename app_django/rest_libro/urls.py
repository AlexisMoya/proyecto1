from django.urls import path
from rest_libro import views
from rest_libro.viewslogin import login
urlpatterns =[

    path('login', login, name='login'),
]