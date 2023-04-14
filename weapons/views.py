from rest_framework import viewsets

from .models import Weapon
from .serializers import WeaponSerializer


class WeaponiewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
