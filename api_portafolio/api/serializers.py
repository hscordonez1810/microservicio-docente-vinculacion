from rest_framework import serializers
from api.models import Solicitud

class   PortafolioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'