from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/enemies/', include('enemies.urls')),
    path('api/players/', include('players.urls')),
    path('api/weapons/', include('weapons.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
