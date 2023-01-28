from rest_framework import viewsets

from api.serializers import PortafolioSerializer
from api.models import Solicitud

class PortafolioViewSet (viewsets.ModelViewSet):
    serializer_class = PortafolioSerializer
    queryset = Solicitud.objects.all()

# Create your views here.
