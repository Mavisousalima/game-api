from rest_framework import viewsets

from .models import Enemy
from .serializers import EnemySerializer


class EnemyViewSet(viewsets.ModelViewSet):
    queryset = Enemy.objects.all()
    serializer_class = EnemySerializer
