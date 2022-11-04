from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from user.serializers import UserCreateSerializer, UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = (
        get_user_model().objects.all()
        .select_related('account')
        .prefetch_related('categories')
    )
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.DjangoModelPermissions)
