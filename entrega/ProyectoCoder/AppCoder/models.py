from django.db import models

# Create your models here.

class Curso(models.Model):
    
    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()

class Profesor(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    experiencia = models.CharField(max_length=2)

class Estudiante(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    edad = models.IntegerField()

class TPractico(models.Model):
    nombreTrabajo = models.CharField(max_length=60)
    entrega = models.DateField()