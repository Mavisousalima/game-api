from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Weapon
from .serializers import WeaponSerializer


class WeaponViewSetTests(APITestCase):
    def setUp(self):
        self.weapon1 = Weapon.objects.create(
            name="Weapon1",
            cooldown=5,
            damage=10
        )
        self.weapon2 = Weapon.objects.create(
            name="Weapon2",
            cooldown=10,
            damage=15
        )
        self.url = reverse('weapon-list')

    def test_get_weapons_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_weapon_detail(self):
        response = self.client.get(
            reverse('weapon-detail', args=[self.weapon1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.weapon1.name)

    def test_create_weapon(self):
        data = {
            'name': 'New Weapon',
            'cooldown': 8,
            'damage': 12
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Weapon.objects.count(), 3)

    def test_update_weapon(self):
        data = {
            'name': 'Updated Weapon',
            'cooldown': 12,
            'damage': 20
        }
        response = self.client.put(
            reverse('weapon-detail', args=[self.weapon1.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.weapon1.refresh_from_db()
        self.assertEqual(self.weapon1.name, 'Updated Weapon')

    def test_delete_weapon(self):
        response = self.client.delete(
            reverse('weapon-detail', args=[self.weapon1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Weapon.objects.count(), 1)
