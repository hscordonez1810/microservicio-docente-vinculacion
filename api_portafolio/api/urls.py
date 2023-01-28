from rest_framework.routers import DefaultRouter
from api.views import PortafolioViewSet

router = DefaultRouter()

router.register('api/portafolio', PortafolioViewSet)

urlpatterns = []

urlpatterns += router.urls