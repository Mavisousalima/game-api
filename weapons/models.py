from django.db import models


class Weapon(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            null=False, blank=False)
    cooldown = models.IntegerField(null=False, blank=False)
    damage = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to='weapons/',
                              default='weapons/weapon_default.png', null=True, blank=True)

    def __str__(self):
        return self.name
