"""
Views for the user API.
"""

from rest_framework import generics
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer
    )

# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer

# replaceble?
class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


