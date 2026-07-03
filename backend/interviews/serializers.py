from rest_framework import serializers
from .models import Interview,Question

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

# question serializer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            "question_number",
            "question_text",
        ]