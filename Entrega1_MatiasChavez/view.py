from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Profesor,Curso


def home(request):
    profesores = Profesor.objects.all()
    cursos = Curso.objects.all()
    return render(request, "home.html",{"profesores":profesores,"cursos":cursos })