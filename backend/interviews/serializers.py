from rest_framework import serializers
from .models import Interview

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = [
            "id",
            "role",
            "difficulty",
            "status",
            "score",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "status",
            "score",
            "created_at",
        ]