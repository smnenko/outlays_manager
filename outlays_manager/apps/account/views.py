from rest_framework import generics, permissions

from account.models import Account
from account.serializers import AccountSerializer


class AccountAPIView(generics.RetrieveAPIView):
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.DjangoModelPermissions)

    def get_object(self):
        account = Account.objects.get(user=self.request.user)
        self.check_object_permissions(self.request, account)
        return account
