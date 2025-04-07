from django.db import models

# Create your models here.

from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    programa = models.CharField(max_length=100)
    semestre = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"