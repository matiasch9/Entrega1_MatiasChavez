
from django.urls import path
from AppCoder.view import *

urlpatterns = [
    path('Estudiantes/', Estudiantes),
    path('Cursos/', Cursos),
    path('Profesores/', Profesores),
    path('buscar_estudiante/', buscar_estudiante),
]