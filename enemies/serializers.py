from rest_framework import serializers

from .models import Enemy


class EnemySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enemy
        fields = '__all__'
