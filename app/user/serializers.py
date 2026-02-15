"""
Serializer for the user API View.
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    # Add UniqueValidator to ensure duplicate emails return 400
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=get_user_model().objects.all())]
    )

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)
