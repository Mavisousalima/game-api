from django.db import models


class Enemy(models.Model):
    ATTACK_CHOICES = (
        ("slash", "Slash"),
        ("claw", "Claw"),
        ("thunder", "Thunder"),
        ("leaf_attack", "Leaf Attack")
    )

    ATTACK_SOUND_CHOICES = (
        ("../audio/attack/slash.wav", "Slash"),
        ("../audio/attack/claw.wav", "Claw"),
        ("../audio/attack/fireball.wav", "Fireball")
    )

    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False
    )
    image = models.ImageField(
        upload_to='enemies/', default='enemies/enemy_default.png', null=True, blank=True)
    health = models.IntegerField(default=1, blank=False, null=False)
    exp = models.IntegerField(default=1, blank=False, null=False)
    damage = models.IntegerField(default=1)
    attack_type = models.CharField(
        max_length=100,
        choices=ATTACK_CHOICES,
        blank=False,
        null=False
    )
    attack_sound = models.CharField(
        max_length=255,
        choices=ATTACK_SOUND_CHOICES,
        blank=False,
        null=False
    )
    speed = models.FloatField(default=1, blank=False, null=False)
    resistance = models.IntegerField(default=3, blank=False, null=False)
    attack_radius = models.IntegerField(default=50, blank=False, null=False)
    notice_radius = models.IntegerField(default=300, blank=False, null=False)

    def __str__(self):
        return self.name

    def image_url(self):
        return self.image.url if self.image else None
