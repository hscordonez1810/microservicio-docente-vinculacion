from rest_framework import serializers
from api.models import Solicitud

class   SolicitudSerializer (serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'