from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'gender', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Remove the password from the validated data
        password = validated_data.pop('password', None)
        # Create the user instance
        user = User(**validated_data)
        # Hash the password
        if password is not None:
            user.set_password(password)
        # Save the user instance
        user.save()
        return user
