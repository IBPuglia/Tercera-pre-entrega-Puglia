from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def curso(request):

    return render(request, "AppCoder/cursada.html")

def estudiante(request):

    return render(request, "AppCoder/estudiante.html")

def profesor(request):

    return render(request, "AppCoder/profesor.html")

def tpractico(request):

    return render(request, "AppCoder/tpractico.html")

def cursoformulario(request):
    
    if request.method == "POST":

        formulario1 = CursoFormulario(request.POST)
        
        if formulario1.is_valid():

            info = formulario1.cleaned_data
            curso = Curso(nombre=info["curso"], camada=info["camada"])
            curso.save()
            return render(request, "AppCoder/Inicio.html")
        
    else:

        formulario1 = CursoFormulario()

    return render(request, "AppCoder/cursoFormulario.html", {"form1":formulario1})

def buscarCamada(request):

    return render(request, "AppCoder/inicio.html")

def resultados(request):

    if request.GET["camada"]:

        camada=request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})
    
    else:

        respuesta="No enviaste datos."

    return HttpResponse(respuesta)