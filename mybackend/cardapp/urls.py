from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from .views import CardList

urlpatterns = [
    path('admin', admin.site.urls),
    path('', CardList.as_view(), name='card-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
