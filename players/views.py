from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

from .models import Player
from .serializers import PlayerSerializer, PlayerUpdateSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return PlayerUpdateSerializer
        else:
            return PlayerSerializer


class LoginViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(methods=['post'], detail=False)
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)

        if not user:
            return Response({'error': 'Invalid email or password'},
                            status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'image': user.image.url,
            'health': user.health,
            'energy': user.energy,
            'speed': user.speed,
            'money': user.money,
            'exp': user.exp,
        }, status=status.HTTP_200_OK)


class RankingViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Player.objects.all().order_by('-exp')

        serializer = PlayerSerializer(queryset, many=True)

        return Response(serializer.data)
