from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Estudiante,Curso,Profesor

# Create your views here.


def Estudiantes(request):
    if request.method == "POST":
        if(request.POST['nombre']==""or request.POST['apellido']=="" or request.POST['email']==""):
            return render(request, "Estudiantes.html", {"aux": "Falto agregar un valor"}) 
        else:
            estudiante =  Estudiante(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
            estudiante.save()
            return render(request, "Estudiantes.html", {"aux": "Agregado correctamente"})
    return render(request, "Estudiantes.html")



def Profesores(request):
    if request.method == "POST":
        if(request.POST['nombre']==""or request.POST['apellido']=="" or request.POST['email']=="" or request.POST['profesion']==""):
            return render(request, "Profesores.html", {"aux": "Falto agregar un valor"}) 
        else:
            profesor =  Profesor(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'], profesion = request.POST['profesion'])
            profesor.save()
            return render(request, "Profesores.html", {"aux": "Agregado correctamente"})
    return render(request, "Profesores.html")



def Cursos(request):
    if request.method == "POST":
        if(request.POST['nombre']==""or request.POST['camada']==""):
            return render(request, "Cursos.html", {"aux": "Falto agregar un valor"}) 
        else:
            curso =  Curso(nombre = request.POST['nombre'], camada = request.POST['camada'])
            curso.save()
            return render(request, "Cursos.html", {"aux": "Agregado correctamente"})
    return render(request, "Cursos.html")

def Entregable(request):
    return render(request, "Entregable.html")