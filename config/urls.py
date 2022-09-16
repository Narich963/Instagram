from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from instagram.views import PostViewSet, ProfileViewset
from .urls_yasg import urlpatterns_yasg

router = routers.DefaultRouter()

router.register(r'post' ,PostViewSet)
router.register(r'profile', ProfileViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('instagram.urls'))
] + urlpatterns_yasg + router.urls +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
