from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "full_name",
            "role",
            "experience_level",
            "subscription_plan",
        ]

        extra_kwargs = {
            "password" : {"write_only": True}
        }

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)