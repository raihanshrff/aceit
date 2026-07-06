from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Interview,Question,Answer
from .serializers import InterviewSerializer, QuestionSerializer,AnswerSerializer
# Create your views here.

class InterviewCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = InterviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class QuestionCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,interview_id):
        questions = Question.objects.filter(
            interview_id = interview_id
        ).order_by("question_number")

        serializer = QuestionSerializer(
            questions,
            many=True
        )
        return Response(serializer.data)
    
# Answermodel views
class SubmitAnswerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.validated_data["question"]
            if Answer.objects.filter(question=question).exists():
                return Response(
                    {"error":"Answer already submitted for this question"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if question.interview.user != request.user:
                return Response(
                    {"error":"permission denied"},
                    status=status.HTTP_403_FORBIDDEN
                )
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )