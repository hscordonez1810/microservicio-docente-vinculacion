from rest_framework.routers import DefaultRouter
from api.views import SolicitudViewSet,PersonaViewSet,TipoPersonaCatalogoViewSet,CatalogoViewSet,FundacionSerializer,PortafolioSerializer,UserSerializer

router = DefaultRouter()

router.register('api/solicitud', SolicitudViewSet)
router.register('api/fundacion', FundacionSerializer)
router.register('api/persona', PersonaViewSet)
router.register('api/tipo-persona',TipoPersonaCatalogoViewSet )
router.register('api/catalogo',CatalogoViewSet )
router.register('api/portafolio',PortafolioSerializer )
router.register('api/users',UserSerializer )

urlpatterns = []

urlpatterns += router.urls