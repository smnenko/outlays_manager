from rest_framework import viewsets, permissions

from transaction.models import Transaction
from transaction.serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.DjangoModelPermissions)

    def get_queryset(self):
        return Transaction.objects.filter(account=self.request.user.account)
