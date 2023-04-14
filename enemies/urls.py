from rest_framework.routers import DefaultRouter

from .views import EnemyViewSet


router = DefaultRouter()
router.register(r'', EnemyViewSet)

urlpatterns = router.urls
