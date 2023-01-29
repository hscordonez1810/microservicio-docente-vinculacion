from api.models import Catalogo, TipoPersonaCatalogo, Persona, Portafolio, Fundacion, User, Solicitud
from api.serializers import CatalogoSerializer, TipoPersonaCatalogoSerializer, PersonaSerializer, FundacionSerializer, UserSerializer, PortafolioSerializer, SolicitudSerializer
from rest_framework import viewsets



class SolicitudViewSet (viewsets.ModelViewSet):
    serializer_class = SolicitudSerializer
    queryset = Solicitud.objects.all()

class PersonaViewSet (viewsets.ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()

class CatalogoViewSet (viewsets.ModelViewSet):
    serializer_class = CatalogoSerializer
    queryset = Catalogo.objects.all()

class TipoPersonaCatalogoViewSet (viewsets.ModelViewSet):
    serializer_class = TipoPersonaCatalogoSerializer
    queryset = TipoPersonaCatalogo.objects.all()

class PortafolioViewSet (viewsets.ModelViewSet):
    serializer_class = PortafolioSerializer
    queryset = Portafolio.objects.all()
    
class FundacionViewSet (viewsets.ModelViewSet):
    serializer_class = FundacionSerializer
    queryset = Fundacion.objects.all()
    
class UserViewSet (viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
# Create your views here.