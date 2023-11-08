
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('task/', include('tasks.urls')),
    path('api/', include('api_view.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
