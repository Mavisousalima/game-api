from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Enemy
from .serializers import EnemySerializer


class EnemyViewSetTests(APITestCase):
    def setUp(self):
        self.enemy1 = Enemy.objects.create(
            name="Enemy1",
            health=100,
            exp=50,
            damage=10,
            attack_type="slash",
            attack_sound="../audio/attack/slash.wav",
            speed=1.5,
            resistance=3,
            attack_radius=50,
            notice_radius=300
        )
        self.enemy2 = Enemy.objects.create(
            name="Enemy2",
            health=200,
            exp=100,
            damage=20,
            attack_type="claw",
            attack_sound="../audio/attack/claw.wav",
            speed=1.2,
            resistance=5,
            attack_radius=70,
            notice_radius=200
        )
        self.url = reverse('enemy-list')

    def test_get_enemies_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_enemy_detail(self):
        response = self.client.get(
            reverse('enemy-detail', args=[self.enemy1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.enemy1.name)

    def test_create_enemy(self):
        data = {
            'name': 'New Enemy',
            'health': 150,
            'exp': 75,
            'damage': 15,
            'attack_type': 'thunder',
            'attack_sound': '../audio/attack/fireball.wav',
            'speed': 1.8,
            'resistance': 4,
            'attack_radius': 60,
            'notice_radius': 250
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Enemy.objects.count(), 3)

    def test_update_enemy(self):
        data = {
            'name': 'Updated Enemy',
            'health': 120,
            'exp': 60,
            'damage': 12,
            'attack_type': 'leaf_attack',
            'attack_sound': '../audio/attack/slash.wav',
            'speed': 1.6,
            'resistance': 2,
            'attack_radius': 40,
            'notice_radius': 275
        }
        response = self.client.put(
            reverse('enemy-detail', args=[self.enemy1.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.enemy1.refresh_from_db()
        self.assertEqual(self.enemy1.name, 'Updated Enemy')

    def test_delete_enemy(self):
        response = self.client.delete(
            reverse('enemy-detail', args=[self.enemy1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Enemy.objects.count(), 1)
