
from django.urls import path
from AppCoder.view import *

urlpatterns = [
    path('Estudiantes/', Estudiantes),
    path('Entregable/', Entregable),
    path('Cursos/', Cursos),
    path('Profesores/', Profesores),
]