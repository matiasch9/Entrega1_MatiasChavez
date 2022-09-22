from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Profesor


def home(request):
    data = Profesor.objects.all()
    return render(request, "home.html",{"data":data})