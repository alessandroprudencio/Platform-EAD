
from django.contrib import admin
from platform_ead.core import views
from platform_ead.courses import views
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('platform_ead.core.urls')),
    path('conta/', include('platform_ead.accounts.urls')),
    path('cursos/', include('platform_ead.courses.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)