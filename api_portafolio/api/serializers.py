from rest_framework import serializers
from api.models import Solicitud, Catalogo, TipoPersonaCatalogo, Persona, Portafolio, Fundacion, User

class   SolicitudSerializer (serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'
        
class  PersonaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
    
class   CatalogoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Catalogo
        fields = '__all__'
        
        
class   TipoPersonaCatalogoSerializer (serializers.ModelSerializer):
    class Meta:
        model = TipoPersonaCatalogo
        fields = '__all__'

class   PortafolioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Portafolio
        fields = '__all__'

class FundacionSerializer(serializers.ModelSerializer):
    class Meta:
         model = Fundacion
         fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'