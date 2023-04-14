from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin

from .models import Player


class PlayerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Player
        fields = '__all__'


class PlayerChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Player


class PlayerAdmin(UserAdmin):
    add_form = PlayerCreationForm
    form = PlayerChangeForm
    model = Player
    list_display = ('email', 'name', 'health', 'is_active',
                    'is_superuser', 'is_staff')
    list_filter = ('is_active', 'is_superuser', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {
            'fields': (
                'name', 'image',
                'health', 'energy', 'money', 'exp', 'speed'
            )}
         ),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important Dates', {'fields': ('date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'image', 'is_active', 'is_staff', 'is_superuser')}
         ),
    )

    ordering = ('email',)


admin.site.register(Player, PlayerAdmin)
