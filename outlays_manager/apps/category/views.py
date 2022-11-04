from rest_framework import viewsets, permissions

from category.models import Category
from category.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated, permissions.DjangoModelPermissions)

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
