from rest_framework.routers import DefaultRouter
from api.views import SolicitudViewSet,PersonaViewSet,TipoPersonaCatalogoViewSet,CatalogoViewSet,FundacionViewSet,PortafolioViewSet,UserViewSet

router = DefaultRouter()

router.register('api/solicitud', SolicitudViewSet)
router.register('api/persona', PersonaViewSet)
router.register('api/catalogo',CatalogoViewSet)
router.register('api/tipo-persona',TipoPersonaCatalogoViewSet)
router.register('api/portafolio',PortafolioViewSet)
router.register('api/fundacion', FundacionViewSet)
router.register('api/users',UserViewSet )

urlpatterns = []

urlpatterns += router.urls