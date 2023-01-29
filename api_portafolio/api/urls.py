from rest_framework.routers import DefaultRouter
from api.views import SolicitudViewSet,PersonaViewSet

router = DefaultRouter()

router.register('api/portafolio', SolicitudViewSet)

router.register('api/persona', PersonaViewSet)

urlpatterns = []

urlpatterns += router.urls