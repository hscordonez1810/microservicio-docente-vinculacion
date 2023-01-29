from django.db import models

class Solicitud (models.Model):
    estado= models.BooleanField()
    tipo_solicitud = models.CharField(max_length=15)
    fecha_emision =  models.DateField(auto_now=False,auto_now_add=False)
    
class Persona(models.Model):
    nombre = models.CharField(max_length=60)
    cedula = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=70)
# Create your models here.
