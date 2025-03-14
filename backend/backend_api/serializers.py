from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    """
    UserSerializer is a Django REST framework serializer for the User model.
    It serializes the fields 'id', 'username', and 'password' of the User model.
    The 'password' field is write-only, meaning it will not be included in the serialized representation of the User object.
    Methods:
        create(validated_data):
            Creates and returns a new User instance using the validated data.
    """

    class Meta:
        """
        Meta class for the User serializer.
        Attributes:
            model (django.db.models.Model): The model that is being serialized.
            fields (list): List of fields to be included in the serialization.
            extra_kwargs (dict): Dictionary of additional keyword arguments for specific fields.
        """

        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        Create and return a new User instance, given the validated data.
        Args:
            validated_data (dict): The validated data containing user information.
        Returns:
            User: The newly created User instance."
        """
        # Validated data is passed in as a dictionary
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Meta class for the Note serializer.
        Attributes:
            model (django.db.models.Model): The model that is being serialized.
            fields (list): List of fields to be included in the serialization.
            extra_kwargs (dict): Dictionary of additional keyword arguments for specific fields.
        """

        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}
