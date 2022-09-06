"""
Vitas para la API de usuarios
"""
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from user.serializers import UserSerializers, AuthTokenSerializer
from rest_framework.settings import api_settings


class CreateUserView(generics.CreateAPIView):
    """Crear un nuevo usuario en el sistema."""
    serializer_class = UserSerializers

class CreateTokenView(ObtainAuthToken):
    """ Create a new auth token for user """
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES