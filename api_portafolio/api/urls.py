from rest_framework.routers import DefaultRouter
from api.views import SolicitudViewSet,PersonaViewSet,TipoPersonaCatalogoViewSet,CatalogoViewSet

router = DefaultRouter()

router.register('api/solicitud', SolicitudViewSet)

router.register('api/persona', PersonaViewSet)

router.register('api/tipo-persona',TipoPersonaCatalogoViewSet )
router.register('api/catalogo',CatalogoViewSet )

urlpatterns = []

urlpatterns += router.urls