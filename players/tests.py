from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Player


class PlayerTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_player(self):
        data = {
            'email': 'test@example.com',
            'name': 'Test Player',
            'health': 100,
            'energy': 100,
            'speed': 5,
            'exp': 0,
            'money': 0,
            'position_x': 0,
            'position_y': 0,
            'is_active': True,
            'is_superuser': False,
            'is_staff': False
        }
        response = self.client.post('/api/players/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_player(self):
        player = Player.objects.create(
            email='test@example.com',
            name='Test Player',
            health=100,
            energy=100,
            speed=5,
            exp=0,
            money=0,
            position_x=0,
            position_y=0,
            is_active=True,
            is_superuser=False,
            is_staff=False
        )
        response = self.client.get(f'/api/players/{player.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_player(self):
        player = Player.objects.create(
            email='test@example.com',
            name='Test Player',
            health=100,
            energy=100,
            speed=5,
            exp=0,
            money=0,
            position_x=0,
            position_y=0,
            is_active=True,
            is_superuser=False,
            is_staff=False
        )
        data = {
            'name': 'Updated Player',
            'health': 90,
            'energy': 80,
            'speed': 6
        }
        response = self.client.patch(f'/api/players/{player.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        player.refresh_from_db()
        self.assertEqual(player.name, 'Updated Player')

    def test_delete_player(self):
        player = Player.objects.create(
            email='test@example.com',
            name='Test Player',
            health=100,
            energy=100,
            speed=5,
            exp=0,
            money=0,
            position_x=0,
            position_y=0,
            is_active=True,
            is_superuser=False,
            is_staff=False
        )
        response = self.client.delete(f'/api/players/{player.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Player.DoesNotExist):
            player.refresh_from_db()
