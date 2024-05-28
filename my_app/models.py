from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad}"