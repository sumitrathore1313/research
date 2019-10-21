# Create a router and register our viewsets with it.
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import WordNetViewSet

router = DefaultRouter()
router.register(r'word-net/', WordNetViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]