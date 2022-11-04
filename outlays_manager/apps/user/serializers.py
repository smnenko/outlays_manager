from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from account.serializers import AccountSerializer
from category.models import Category
from category.constants import DEFAULT_USER_CATEGORIES
from category.serializers import CategorySerializer
from user.constants import DEFAULT_USER_PERMISSIONS


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
            'password',
            'password_confirm'
        )

    def validate(self, attrs):
        if attrs.get('password') == attrs.get('password_confirm'):
            attrs.pop('password_confirm')
            return attrs
        raise ValidationError('Passwords don\'t match')

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        if not Group.objects.filter(name='Users').exists():
            group = Group.objects.create(name='Users')
            group.permissions.set(Permission.objects.filter(codename__in=DEFAULT_USER_PERMISSIONS))
        else:
            group = Group.objects.get(name='Users')
        user.groups.add(group)
        Category.objects.bulk_create([Category(name=i, user=user) for i in DEFAULT_USER_CATEGORIES])
        return user


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    categories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = get_user_model()
        exclude = ('password',)
