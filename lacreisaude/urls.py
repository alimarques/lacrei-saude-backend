from rest_framework.routers import DefaultRouter

from .views import ConsultaViewSet, ProfissionalViewSet

app_name = 'lacreisaude'

router = DefaultRouter(trailing_slash=False)
router.register(r'profissionais', ProfissionalViewSet)
router.register(r'consultas', ConsultaViewSet)

urlpatterns = router.urls