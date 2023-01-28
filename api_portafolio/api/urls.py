from rest_framework.routers import DefaultRouter
from api.views import PortafolioViewSet

router = DefaultRouter()

router.register('api/Portafolio', PortafolioViewSet)

urlpatterns = []

urlpatterns += router.urls