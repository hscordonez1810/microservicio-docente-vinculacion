from django.db import models

class Solicitud (models.Model):
    estado= models.BooleanField()
    tipo_solicitud = models.CharField(max_length=15)
    
class Catalogo (models.Model):
    rol_docente_vinculacion = models.IntegerField()
    rol_docente_tutor = models.IntegerField()
    rol_estudiante = models.IntegerField()
    rol_coordinador_general = models.IntegerField()
    rol_voordinador_carrera = models.IntegerField()

class Persona(models.Model):
    nombre = models.CharField(max_length=60)
    cedula = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=70)
    
class User (models.Model):
    usuario = models.CharField(max_length=20)
    clave = models.CharField(max_length=20)

class TipoPersonaCatalogo (models.Model):
    semestre = models.CharField(max_length=15)
    carrera = models.CharField(max_length=25)    
    jornada = models.CharField(max_length=10)
    catalogo = models.ForeignKey(Catalogo, on_delete=models.PROTECT)
    idPersona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    
class Portafolio (models.Model):
    nombre_archivo = models.CharField(max_length=60)
    opciones = models.CharField(max_length=10)
    observaciones = models.CharField(max_length=10)
    aprobar = models.BooleanField(default=False)
    dirigido = models.BooleanField(default=False)
    estado = models.BooleanField(default=False)
    idTipoPersona = models.ForeignKey(TipoPersonaCatalogo, on_delete=models.PROTECT)

class Fundacion (models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=70)
    encargado = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10)
    estado = models.BooleanField(default=False)
    idTipoPersona = models.ForeignKey(TipoPersonaCatalogo, on_delete=models.PROTECT)
# Create your models here.