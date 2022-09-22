from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Estudiantes(request):
    if request.method == "POST":
       estudiante =  Estudiante(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
       estudiante.save()
       return render(request, "home.html")
    return render(request, "Estudiantes.html")

def Entregable(request):
    return render(request, "Entregable.html")

def Profesor(request):
    return render(request, "Profesor.html")

def Curso(request):
    return render(request, "Curso.html")

def buscar_estudiante(request):
    if request.GET["email"]:
        email = request.GET["email"]
        estudiantes = Estudiante.objects.filter(email__icontains = email) 
        return render(request, "Estudiantes.html", {"estudiantes": estudiantes})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)