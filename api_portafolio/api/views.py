from rest_framework import viewsets

from api.serializers import SolicitudSerializer,PersonaSerializer
from api.models import Solicitud,Persona

class SolicitudViewSet (viewsets.ModelViewSet):
    serializer_class = SolicitudSerializer
    queryset = Solicitud.objects.all()
    

class PersonaViewSet (viewsets.ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()

# Create your views here.
