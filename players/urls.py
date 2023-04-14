from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import PlayerViewSet, LoginViewSet, RankingViewSet


router = DefaultRouter()
router.register(r'', PlayerViewSet)

urlpatterns = [
    path('login/', LoginViewSet.as_view({'post': 'login'}), name='login'),
    path('ranking/', RankingViewSet.as_view({'get': 'list'}), name='ranking')
] + router.urls
