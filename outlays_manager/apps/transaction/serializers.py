from rest_framework import serializers

from transaction.models import Transaction
from category.serializers import CategorySerializer


class TransactionSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'
