
from django.urls import path
from AppCoder.view import *

urlpatterns = [
    path('Estudiantes/', Estudiantes),
    path('Entregable/', Entregable),
    path('Curso/', Curso),
    path('Profesores/', Profesores),
]