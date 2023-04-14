from rest_framework.routers import DefaultRouter

from .views import WeaponiewSet


router = DefaultRouter()
router.register(r'', WeaponiewSet)

urlpatterns = router.urls
