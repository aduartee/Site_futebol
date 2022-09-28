from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from site_futebol.settings import STATICFILES_DIRS
from django.conf.urls.static import static

urlpatterns = [
    path('', include('futebol.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
