from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("cursada/", curso, name="Curso"),
    path("profesor", profesor, name="Profes"),
    path("estudiante", estudiante, name="Estudiantes"),
    path("tpractico", tpractico, name="Entregas"),
    path("cursoFormulario/", cursoformulario, name="Formulario"),
    path("buscarCamada/", buscarCamada, name="BuscarCamada"),
    path("resultados/", resultados, name="ResultadoBusqueda"),
]