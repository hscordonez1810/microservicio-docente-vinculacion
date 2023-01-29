from rest_framework import serializers
from api.models import Solicitud, Catalogo, TipoPersonaCatalogo, Persona, Portafolio, Fundacion, User

class   SolicitudSerializer (serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = 'all'
        
class  PersonaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = 'all'
    
class   CatalogoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Catalogo
        fields = '_all_'
        
        
class   TipoPersonaCatalogoSerializer (serializers.ModelSerializer):
    class Meta:
        model = TipoPersonaCatalogo
        fields = '_all_'

class   PortafolioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Portafolio
        fields = 'all'

class FundacionSerializer(serializers.ModelSerializer):
    class Meta:
         model = Fundacion
         fields = 'all'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'all'