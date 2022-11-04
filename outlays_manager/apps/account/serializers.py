from rest_framework import serializers

from account.models import Account
from transaction.serializers import TransactionSerializer


class AccountSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(read_only=True, many=True)

    class Meta:
        model = Account
        fields = '__all__'
