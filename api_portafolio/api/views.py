from rest_framework import viewsets
from api.models import Portafolio
from api.serializers import PortafolioSerializer

class PortafolioViewSet (viewsets.ModelViewSet):
    serializer_class = PortafolioSerializer
    queryset = Portafolio.objects.all()

# Create your views here.
