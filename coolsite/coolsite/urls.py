from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from cookie.views import *
from django.urls import include
from coolsite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cookie.urls')), #передает все зависимости
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound

