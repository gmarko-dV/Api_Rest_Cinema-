from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, DirectorViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'directors', DirectorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
