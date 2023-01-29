from rest_framework import serializers
from api.models import Solicitud, Persona

class   SolicitudSerializer (serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'
        
class  PersonaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'